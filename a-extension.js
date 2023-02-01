class a-extention {
getInfo() {
    return{
"id": "a-extention",
"name" : "A Extention",
"blocks" :[
    {
        "opcode": "true", //This will be the ID code for the block
        "blockType": "Boolean", //This can either be Boolean, reporter, command, or hat
        "text": "true", //This is the block text, and how it will display in the Scratch interface
        "arguments": {}
        }
    },
],
"menus": {}
    };
}
substringy({}) { 
return true;
}
}
Scratch.extensions.register(new a-extention());
