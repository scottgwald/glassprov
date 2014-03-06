Stage-Displays
-----------------------------------------

ws.publish("glassprov", {user: "kevin.b.tu", glass:"1", command: "showline", line: "What's my line"});
ws.publish("glassprov", {user: "scottgwald", glass:"2", command: "playvideo", line: "vid001.mp4"});


Keyword: "glassprov"

User: username
glass: 1-4 (Which quadrant to display in)
command: "showline" or "playvideo"
line: text to display or video id