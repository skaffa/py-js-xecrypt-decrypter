function XUcrypt(XEcryptString) {
    var XEcryptValues = XEcryptString.substring(1).split(".");  //remove first "." character and put numbers into array
    var XEcryptChars = []; //create array for encrypted characters
    var modeMap = {}; //create map of array occurrences
    var maxCount = 1; //create count var for tracking highest
    var mode; //create mode var to keep track of which is the highest occurring character
    var decoded = ""; //create decoded var for the decoded string
    /*loop adds sum of each group of three numbers to array and creates a map of the values and the number of times they
    occur in order to calculate the mode-average which _should_ be the space character*/
    for (var i = 0; i < XEcryptValues.length / 3; i++) {
        var j = 0;
        for (var k = 0; k < 3; k++) {
            j += parseInt(XEcryptValues[k+3*i]);
        }
        XEcryptChars[i] = j;
        if (modeMap[j] == null) {
            modeMap[j] = 1;
        } else {
            modeMap[j]++;
            if (modeMap[j] > maxCount) {
                maxCount = modeMap[j];
                mode = j;
            }
        }
    }
    var key = mode-32; //the key is the number of the mode common encrypted charater minus the ASCII code for a space
    for (var i=0; i<XEcryptChars.length; i++) { //for every array entry, type the decoded ascii character
        decoded += String.fromCharCode(XEcryptChars[i]-key);
    }
    return decoded;
}
