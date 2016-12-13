function* genLucky() {
    i = 0;
    while (true) {
        i = i+1;
        t = i.toString();
        if (t.indexOf("13") || t.endsWith("4")){

            continue;
        }
        yield i;
    }
}

for (i=0; i<100; i++) {
    g = genLucky();
    console.log(g.next())}
