from django.shortcuts import render
from .models import Line, Emotion, Clip, PledgeBreak1, PledgeBreak2, PartyQuirk, Location, Style, Noun, Quirk, Celebrity

import random
from django.views.decorators.http import require_http_methods

#begin serializer https://github.com/Strangemother/django-djasoner
from io import StringIO
from django.views.decorators.csrf import csrf_exempt
import json
import datetime

try:

    from django.db.models import Model
    from django.db.models.query import QuerySet
    from django.utils.encoding import smart_unicode
    from django.utils.simplejson import dumps
    from django.utils import simplejson
    # from datetime import datetime, date
    from django.http import HttpResponse
    from django.shortcuts import render_to_response
    from django.conf import settings

except ImportError:
    django_lib = False
else:
    django_lib = True
    # no django

class Error(Exception):
    ''' Base class for exceptions in this module'''
    pass

class NoDjangoError(Error):
    '''Exception raised for missing django modules'''
    def __init__(self, value):
        self.value = value

"""
from serializers import to_json(data, **options)
"""

def model_json(queryset, fields_tuple=None):
    if django_lib:
        from django.core import serializers as srl
        return srl.serialize('json', queryset, fields=fields_tuple)
    else:
        raise NoDjangoError('''Cannot use django.core.serializers as Django is
                            not installed.''')

def model_json_response(queryset, fields_tuple=None):
    data = model_json(queryset, fields_tuple)
    return HttpResponse(
            data,
            content_type = 'application/javascript; charset=utf8'
        )

def json_response(something):
    '''return Simple json dumps() wrapped by a django HttpResponse'''
    o = []
    o.append(something)
    return HttpResponse(
        simplejson.dumps(o),
        content_type = 'application/javascript; charset=utf8'
    )

def json_serialize(object, nested=False):
    '''serialize a python object'''
    js = JSONSerializer()
    j = js.serialize(object, nested=nested)
    
    return j

def json_serialize_response(object, *args, **kwargs):
    ''' Eveoke the serializer and return a django HttpResponse'''
    r = json_serialize(object, *args, **kwargs)
    return HttpResponse(r, mimetype='application/json')

def to_json(data, **options):
    ''' Convery the data to JSON
    return is JSON'''
    js = JSONSerializer()
    j = js.serialize(object, options)

    return j

class UnableToSerializeError(Exception):
    """ Error for not implemented classes """
    def __init__(self, value):
        self.value = value
        Exception.__init__(self)

    def __str__(self):
        return repr(self.value)

'''
If there are fields requiring serialization,
pass a list of SerializeEntities to
'''
class SerializeEntity():

    def __init__(self, search, replacement):
        self.needle = search
        self.replacement = replacement

    def __unicode__(self):
        return u'%s' % self.needle
    
'''    
>>> from json import loads
>>> from pprint import pprint
>>> from core.serializers import json_serialize
>>> x = { 'bananas': 'blue' }
>>> s= json_serialize(x)
>>> cs = loads(s)
>>> pprint(cs) 
'''
class JSONSerializer():
    boolean_fields = ['BooleanField', 'NullBooleanField']
    datetime_fields = ['DatetimeField', 'DateField', 'TimeField']
    number_fields = ['IntegerField', 'AutoField', 'DecimalField', 'FloatField', 'PositiveSmallIntegerField']

    def serialize(self, obj, *args, **options):
        self.options = options

        self.stream = options.pop("stream", StringIO())
        self.selectedFields = options.pop("fields", options.get('fields', None))
        self.ignoredFields = options.pop("ignored", options.get('ignored', None))
        self.use_natural_keys = options.pop("use_natural_keys", options.get("use_natural_keys", False))
        self.transcript = options.pop("transcript", options.get("transcript", {}))
        self.nested = options.pop('nested', False)
        self.currentLoc = ''

        # Placeholder for the later used parser
        self.html_parser = None

        # Escape all string information to be written to the output
        # stream though HTML parser, making it safe to transport.
        # Remove this feature for speed - warn; your JSON may be invalid if False
        self.parse_html = options.pop('parse_html', False)

        # Stack recursive list.
        self.recurse_list = []
        
        self.level = 0

        self.start_serialization()

        self.handle_object(obj)

        self.end_serialization()
        return self.getvalue()

    def get_string_value(self, obj, field):
        """Convert a field's value to a string."""
        return smart_unicode(field.value_to_string(obj))

    def start_serialization(self):
        """Called when serializing of the queryset starts."""
        pass

    def end_serialization(self):
        """Called when serializing of the queryset ends."""
        pass

    def start_array(self):
        """Called when serializing of an array starts."""
        self.stream.write(u'[')
    def end_array(self):
        """Called when serializing of an array ends."""
        self.stream.write(u']')

    def start_object(self):
        """Called when serializing of an object starts."""
        self.stream.write(u'{')

    def end_object(self):
        """Called when serializing of an object ends."""
        self.stream.write(u'}')

    def handle_object(self, object):
        """ Called to handle everything, looks for the correct handling """
        if isinstance(object, dict):
            self.handle_dictionary(object)

        elif isinstance(object, list):
            self.handle_list(object)

        elif isinstance(object, Model):
            self.handle_model(object)

        elif isinstance(object, QuerySet):
            self.handle_queryset(object)

        elif isinstance(object, bool):
            self.handle_simple(object)

        elif isinstance(object, int) or isinstance(object, float) or isinstance(object, long):
            self.handle_simple(object)

        elif isinstance(object, unicode):
            self.handle_simple(object)

        elif isinstance(object, basestring):
            self.handle_simple(object)

        elif isinstance(object, tuple):
            self.handle_simple(object)

        elif isinstance(object, datetime):
            self.handle_datetime(object)

        elif isinstance(object, date):
            self.handle_date(object)

        elif object == None:
            self.handle_none(object)
        else:
            # If this a seralize entity
            try:
                self.handle_string(object)
            except:
                raise UnableToSerializeError(type(object))

    def handle_dictionary(self, d):
        """Called to handle a Dictionary"""
        i = 0
        self.start_object()
        for key, value in d.iteritems():
            self.currentLoc += key+'.'
            #self.stream.write(unicode(self.currentLoc))
            i += 1
            self.handle_simple(key)
            self.stream.write(u': ')
           
            # recursive care.
            # if id(value) not in self.recurse_list:
            self.recurse_list.append(id(value))
            self.handle_object(value)
            # else:
            #     self.stream.write(u'-1')
           
            if i != len(d):
                self.stream.write(u', ')
            self.currentLoc = self.currentLoc[0:(len(self.currentLoc)-len(key)-1)]
        self.end_object()

    def handle_list(self, l):
        """Called to handle a list"""
        self.start_array()

        for value in l:
            self.handle_object(value)
            if l.index(value) != len(l) -1:
                self.stream.write(u', ')

        self.end_array()

    def handle_datetime(self, d):

        self.start_object()
        self.stream.write(u'"date" : "%s", ' % str(d))
        self.stream.write(u'"day" : "%s", ' % d.day )
        self.stream.write(u'"hour" : "%s", ' % d.hour)
        self.stream.write(u'"microsecond" : "%s", ' % d.microsecond )
        self.stream.write(u'"minute" : "%s", ' % d.minute )
        self.stream.write(u'"month" : "%s", ' % d.month)
        self.stream.write(u'"second" : "%s", ' % d.second)
        self.stream.write(u'"weekday" : "%s", ' % d.weekday())
        self.stream.write(u'"year" : "%s"' % d.year )

        self.end_object()

    def handle_date(self, d):

        self.start_object()
        self.stream.write(u'"day" : %s, ' % d.day )
        self.stream.write(u'"month" : %s, ' % d.month)
        self.stream.write(u'"year" : %s,' % d.year )
        self.stream.write(u'"weekday" : %s, ' % d.weekday())
        self.stream.write(u'"isoformat" : "%s", ' % d.isoformat())
        self.stream.write(u'"ctime" : "%s"' % d.ctime())

        self.end_object()



    def handle_model(self, mod):
        """Called to handle a django Model"""

        try:
            _meta = mod._meta
        except AttributeError as e:
             _meta = None

        if _meta is None:
            # Try a standard object
            self.handle_simple(mod)
        else:
            self.start_object()
            for field in mod._meta.local_fields:
                if field.rel is None:
                    if self.selectedFields is None or field.attname in self.selectedFields or field.attname:
                        if self.ignoredFields is None or self.currentLoc + field.attname not in self.ignoredFields:
                            self.handle_field(mod, field)
                else:
                    if self.selectedFields is None or field.attname[:-3] in self.selectedFields:
                        if self.ignoredFields is None or self.currentLoc + field.attname[:-3] not in self.ignoredFields:
                            self.handle_fk_field(mod, field)
            for field in mod._meta.many_to_many:
                if self.selectedFields is None or field.attname in self.selectedFields:
                    if self.ignoredFields is None or self.currentLoc + field.attname not in self.ignoredFields:
                        self.handle_m2m_field(mod, field)
            self.stream.seek(self.stream.tell()-2)
            self.end_object()

    def handle_queryset(self, queryset):
        """Called to handle a django queryset"""
        self.start_array()
        it = 0
        for mod in queryset:
            it += 1
            self.handle_model(mod)
            if queryset.count() != it:
                self.stream.write(u', ')
        self.end_array()

    def handle_field(self, mod, field):
        """Called to handle each individual (non-relational) field on an object."""
        self.handle_simple(field.name)
        if field.get_internal_type() in self.boolean_fields:
            if field.value_to_string(mod) == 'True':
                self.stream.write(u': true')
            elif field.value_to_string(mod) == 'False':
                self.stream.write(u': false')
            else:
                self.stream.write(u': undefined')
        else:
            self.stream.write(u': ')
            self.handle_simple(field.value_to_string(mod))
        self.stream.write(u', ')

    def handle_fk_field(self, mod, field):
        """Called to handle a ForeignKey field."""
                
        related = getattr(mod, field.name)
        if related is not None:
            if field.rel.field_name == related._meta.pk.name:
                # Related to remote object via primary key
                pk = related._get_pk_val()
            else:
                # Related to remote object via other field
                pk = getattr(related, field.rel.field_name)
        
            d = {
                    'pk': pk,
                }
            if self.use_natural_keys and hasattr(related, 'natural_key'):
                d.update({'natural_key': related.natural_key()})
            if type(d['pk']) == str and d['pk'].isdigit():
                d.update({'pk': int(d['pk'])})
        

            self.handle_simple(field.name)
            self.stream.write(u': ')
            if self.nested:
                self.handle_model(related)
            else:
                self.handle_object(d)
            self.stream.write(u', ')



    def handle_m2m_field(self, mod, field):
        """Called to handle a ManyToManyField."""
        if field.rel.through._meta.auto_created:
            self.handle_simple(field.name)
            self.stream.write(u': ')
            self.start_array()
            hasRelationships = False
            
            #import pdb;pdb.set_trace()

            for relobj in getattr(mod, field.name).iterator():

                hasRelationships = True
                pk = relobj._get_pk_val()

                d = {
                        'pk': pk,
                    }
                
                if self.use_natural_keys and hasattr(relobj, 'natural_key'):
                    d.update({'natural_key': relobj.natural_key()})
                if type(d['pk']) == str and d['pk'].isdigit():
                    d.update({'pk': int(d['pk'])})
                
                if self.nested:
                    self.handle_model(relobj)
                else:
                    self.handle_simple(d)
                self.stream.write(u', ')
            if hasRelationships:
                self.stream.seek(self.stream.tell()-2)
            self.end_array()
            self.stream.write(u', ')


    def safe_string(self, strin):
        ''' Returns a transport ready string. '''
        esc = strin
        # UTF-8 save convert
        if type(strin) != unicode:
            esc = unicode('%s' % strin, "utf-8", errors="replace")
        esc = esc.replace('\n', '')

        # if to parse as HTML
        if self.parse_html:
            esc = cgiesc(esc).encode('ascii', 'xmlcharrefreplace')
        return unicode(esc)


    def handle_simple(self, simple):
        """ Called to handle values that can be handled via simplejson """
        esc = self.safe_string( dumps(simple) )
        self.stream.write(esc)
    

    def handle_string(self, simple):
        esc = self.safe_string(simple)
        self.stream.write( u'"%s"' % esc)


    def handle_none(self, object):
        o = ''
        self.stream.write(u'"%s"' % o)#unicode(dumps(o)))

    def getvalue(self):
        """Return the fully serialized object (or None if the output stream is  not seekable).sss """
        if callable(getattr(self.stream, 'getvalue', None)):
            return self.stream.getvalue()

#end serializer

def serialize(data):
    jsonSerializer = JSONSerializer()
    return jsonSerializer.serialize(data, use_natural_keys=True)


# lines in a hat

@csrf_exempt
@require_http_methods(["POST"])
def createLine(request):
    text = json.loads(request.body)['text']
    data = Line.objects.create(text=text)
    data.save()
    return HttpResponse(serialize(data), content_type="application/json")

@csrf_exempt
@require_http_methods(["GET"])
def getLine(request):
    # WORKS PRIOR TO SHRI'S CHANGES

    # line = Line.objects.all()[random.randint(0, Line.objects.count() - 1)]
    # text = line.text
    # # sadface. How is history maintained?
    # # line.delete()
    # data = {"text": text}
    # # data = {"text":text, "glassid":json.loads(request.body)["glassid"]}
    # return HttpResponse(serialize(data), content_type="application/json")

    # SHRI'S CHANGES, WITH MINOR MODS
    line = Line.objects.all()[random.randint(0, Line.objects.count() - 1)]  
    # line = Line.objects.filter(timestamp=None)[random.randint(0, Line.objects.filter(timestamp=None).count() - 1)]
    text = line.text
    line.timestamp = datetime.datetime.now()
    line.save()
    data = {"text": text}
    # data = {"text":text, "glassid":request.GET["glassid"]}
    #    # WS send to request.GET["glassid"] glass and dashboard here
    return HttpResponse(serialize(data), content_type="application/json")

@csrf_exempt
@require_http_methods(["GET"])
def getAllLines(request):
    data = Line.objects.all()
    return HttpResponse(serialize(data), content_type="application/json")


# jump styles

@csrf_exempt
@require_http_methods(["POST"])
def createEmotion(request):
    text = json.loads(request.body)["text"]
    data = Emotion.objects.create(text=text)
    data.save()
    return HttpResponse(serialize(data), content_type="application/json")

@csrf_exempt
@require_http_methods(["GET"])
def getEmotion(request):
    emotion = Emotion.objects.filter(timestamp=None, id=request.GET["id"])[0]
    text = emotion.text
    emotion.timestamp=datetime.datetime.now()
    emotion.save()
    data = {"text":text}
    # WS: send to all glasses and dashboard here
    return HttpResponse(serialize(data), content_type="application/json")

@csrf_exempt
@require_http_methods(["GET"])
def getAllEmotions(request):
    data = Emotion.objects.all()
    # WS: send to dashboard here
    return HttpResponse(serialize(data), content_type="application/json")

# news room

@csrf_exempt
@require_http_methods(["POST"])
def createClip(request):
    text = json.loads(request.body)["text"]
    data = Clip.objects.create(text=text)
    data.save()
    return HttpResponse(serialize(data), content_type="application/json")

@csrf_exempt
@require_http_methods(["GET"])
def getClip(request):
    clip = Clip.objects.filter(timestamp=None).order_by('-votes')[0]
    text = clip.text
    clip.timestamp = datetime.datetime.now()
    clip.save()
    data = {"text":text, "glassid":request.GET["glassid"]}
    # WS: send to glass request.GET["glassid"] and dashboard here
    return HttpResponse(serialize(data), content_type="application/json")

@csrf_exempt
@require_http_methods(["GET"])
def getAllClips(request):
    data = Clip.objects.all()
    return HttpResponse(serialize(data), content_type="application/json")

@csrf_exempt
@require_http_methods(["GET"])
def wstest(request):
    return render_to_response("wstest.html")

@csrf_exempt
@require_http_methods(["GET"])
def wsline(request):
    line = "Hilarity"
    arg = request.GET.get('line')
    if arg is not None:
        line = arg
    print "Line is " + line
    settings.WSCONN.send(
        'glass',
        'script',
        {'glass.html':
        """
        <script>
        WS.wake();
        WS.activityCreate();
        WS.displayCardTree();
        var tree = new WS.Cards();
        tree.add('%s', 'GlassProv');
        WS.cardTree(tree);
        </script>
        """ % line}
    )
    return render_to_response("wstest.html", {'line': line})

@csrf_exempt
@require_http_methods(["GET"])
def wsline1(request):
    line = "Hilarity"
    arg = request.GET.get('line')
    argID = request.GET.get('glassID')
    if arg is not None:
        line = arg
    print "Line is " + line
    settings.WSCONN.send(
        'glass',
        'script',
        {'glass.html':
        """                                   
        <script>                     
        console.log('myID ' + WSRAW.getGlassID());
        if(WSRAW.getGlassID()=="%s"){
        WS.wake();                                                                                                                                                                          WS.activityCreate();                                                                                                                                                                WS.displayCardTree();                                                                                                                                                 
        var tree = new WS.Cards();                                                                                                                                                          tree.add('%s', 'GlassProv');                                                                                                                                                        WS.cardTree(tree);                                                                                              
        } 
        </script>                                                                                                                                                                    
        """ % (argID, line)}
    )
    return render_to_response("wstest.html", {'line': line})

# lines in a hat

@csrf_exempt
@require_http_methods(["POST"])
def createPartyQuirk(request):
    text = json.loads(request.body)['text']
    data = PartyQuirk.objects.create(text=text)
    data.save()
    return HttpResponse(serialize(data), content_type="application/json")

@csrf_exempt
@require_http_methods(["GET"])
def getPartyQuirk(request):
    line = PartyQuirk.objects.filter(timestamp=None)[random.randint(0, PartyQuirk.objects.filter(timestamp=None).count() - 1)]
    text = line.text
    line.timestamp = datetime.datetime.now()
    line.save()
    data = {"text":text, "glassid":request.GET["glassid"]}
    # WS send to request.GET["glassid"] glass and dashboard here
    return HttpResponse(serialize(data), content_type="application/json")

@csrf_exempt
@require_http_methods(["GET"])
def getAllPartyQuirks(request):
    data = PartyQuirk.objects.all()
    # WS: send to dashboard
    return HttpResponse(serialize(data), content_type="application/json")

# lines in a hat

@csrf_exempt
@require_http_methods(["POST"])
def createPledgeBreak1(request):
    text = json.loads(request.body)['text']
    data = PledgeBreak1.objects.create(text=text)
    data.save()
    return HttpResponse(serialize(data), content_type="application/json")

@csrf_exempt
@require_http_methods(["POST"])
def createPledgeBreak2(request):
    text = json.loads(request.body)['text']
    data = PledgeBreak2.objects.create(text=text)
    data.save()
    return HttpResponse(serialize(data), content_type="application/json")    

@csrf_exempt
@require_http_methods(["GET"])
def getPledgeBreak(request):
    line = PledgeBreak1.objects.filter(timestamp=None, id=request.GET["id1"])[0]
    text = line.text

    line2 = PledgeBreak2.objects.filter(timestamp=None, id=request.GET["id2"])[0]
    text2 = line2.text

    line.timestamp = datetime.datetime.now()
    line2.timestamp = datetime.datetime.now()

    line.save()
    line2.save()

    data = {"text":text, "text2":text2, "glassid":request.GET["glassid"]}
    # WS send to request.GET["glassid"] glass and dashboard here
    return HttpResponse(serialize(data), content_type="application/json")

@csrf_exempt
@require_http_methods(["GET"])
def getAllPledgeBreaks(request):
    pb1 = PledgeBreak1.objects.filter(timestamp=None)
    pb2 = PledgeBreak2.objects.filter(timestamp=None)

    data = {"pb1": pb1, "pb2": pb2}
    # WS send to dashboard here
    return HttpResponse(serialize(data), content_type="application/json")









# NEW STUFF

@csrf_exempt
@require_http_methods(["POST"])
def createLocation(request):
    text = json.loads(request.body)['text']
    data = PartyQuirk.objects.create(text=text)
    data.save()
    return HttpResponse("{}", content_type="application/json")

@csrf_exempt
@require_http_methods(["GET"])
def getLocation(request):
    line = PartyQuirk.objects.filter(timestamp=None)[random.randint(0, PartyQuirk.objects.filter(timestamp=None).count() - 1)]
    text = line.text
    line.timestamp = datetime.datetime.now()
    line.save()
    data = {"text":text, "glassid":request.GET["glassid"]}
    # WS send to request.GET["glassid"] glass and dashboard here                                                                                                                   
    return HttpResponse("{}", content_type="application/json")

@csrf_exempt
@require_http_methods(["GET"])
def getAllLocations(request):
    data = PartyQuirk.objects.all()
    # WS: send to dashboard                                                                                                                                                          
    return HttpResponse("{}", content_type="application/json")



@csrf_exempt
@require_http_methods(["POST"])
def createStyle(request):
    text = json.loads(request.body)['text']
    data = PartyQuirk.objects.create(text=text)
    data.save()
    return HttpResponse("{}", content_type="application/json")

@csrf_exempt
@require_http_methods(["GET"])
def getStyle(request):
    line = PartyQuirk.objects.filter(timestamp=None)[random.randint(0, PartyQuirk.objects.filter(timestamp=None).count() - 1)]
    text = line.text
    line.timestamp = datetime.datetime.now()
    line.save()
    data = {"text":text, "glassid":request.GET["glassid"]}
    # WS send to request.GET["glassid"] glass and dashboard here                                                                                                                    
    return HttpResponse("{}", content_type="application/json")

@csrf_exempt
@require_http_methods(["GET"])
def getAllStyles(request):
    data = PartyQuirk.objects.all()
    # WS: send to dashboard                                    
    return HttpResponse("{}", content_type="application/json")




@csrf_exempt
@require_http_methods(["POST"])
def createNoun(request):
    text = json.loads(request.body)['text']
    data = PartyQuirk.objects.create(text=text)
    data.save()
    return HttpResponse("{}", content_type="application/json")

@csrf_exempt
@require_http_methods(["GET"])
def getNoun(request):
    line = PartyQuirk.objects.filter(timestamp=None)[random.randint(0, PartyQuirk.objects.filter(timestamp=None).count() - 1)]
    text = line.text
    line.timestamp = datetime.datetime.now()
    line.save()
    data = {"text":text, "glassid":request.GET["glassid"]}
    # WS send to request.GET["glassid"] glass and dashboard here                                                                                                                    
    return HttpResponse("{}", content_type="application/json")

@csrf_exempt
@require_http_methods(["GET"])
def getAllNouns(request):
    data = PartyQuirk.objects.all()
    # WS: send to dashboard                                                                                                                           
                                                                                                                              
    return HttpResponse("{}", content_type="application/json")






@csrf_exempt
@require_http_methods(["POST"])
def createQuirk(request):
    text = json.loads(request.body)['text']
    data = PartyQuirk.objects.create(text=text)
    data.save()
    return HttpResponse("{}", content_type="application/json")

@csrf_exempt
@require_http_methods(["GET"])
def getQuirk(request):
    line = PartyQuirk.objects.filter(timestamp=None)[random.randint(0, PartyQuirk.objects.filter(timestamp=None).count() - 1)]
    text = line.text
    line.timestamp = datetime.datetime.now()
    line.save()
    data = {"text":text, "glassid":request.GET["glassid"]}
    # WS send to request.GET["glassid"] glass and dashboard here                                                                                                                     
    return HttpResponse("{}", content_type="application/json")

@csrf_exempt
@require_http_methods(["GET"])
def getAllQuirks(request):
    data = PartyQuirk.objects.all()
    # WS: send to dashboard                                                                                                                                                         \
                                                                                                                                                                                     
    return HttpResponse("{}", content_type="application/json")





@csrf_exempt
@require_http_methods(["POST"])
def createCelebrity(request):
    text = json.loads(request.body)['text']
    data = PartyQuirk.objects.create(text=text)
    data.save()
    return HttpResponse("{}", content_type="application/json")

@csrf_exempt
@require_http_methods(["GET"])
def getCelebrity(request):
    line = PartyQuirk.objects.filter(timestamp=None)[random.randint(0, PartyQuirk.objects.filter(timestamp=None).count() - 1)]
    text = line.text
    line.timestamp = datetime.datetime.now()
    line.save()
    data = {"text":text, "glassid":request.GET["glassid"]}
    # WS send to request.GET["glassid"] glass and dashboard here                                                                                                                     
    return HttpResponse("{}", content_type="application/json")

@csrf_exempt
@require_http_methods(["GET"])
def getAllCelebrities(request):
    data = PartyQuirk.objects.all()
    # WS: send to dashboard                                                                                                                                                         \
                                                                                                                                                                                     
    return HttpResponse("{}", content_type="application/json")
