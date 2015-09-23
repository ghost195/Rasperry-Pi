str = "Line1-abcdef \nLine2-abc \nLine4-abcd";

# entfernt \n aus dem 2ten Wort
print str.split("\n")[2];
print str.split(" ");

# entfernt Line aus dem ersten Wort
print str.split('Line', 1 );
