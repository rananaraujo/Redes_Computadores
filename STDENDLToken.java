package br.ufc.quixada.qxd0025.semantica.frontend.token;

public class STDENDLToken extends Token {
   
    public  STDENDLToken(long line, long start, String value) throws IllegalArgumentException {
        super(line, start, value);
    }



    @Override
    public void interpretAttributes() {
        if(stringValue != null) {
            stringValue = stringValue.substring(0);
        }
    }



    public String getSTDENDLpecialsymbols(){
        interpretAttributes();

        return stringValue;


    }
    @Override
    public String getTokenIdentifier() {
        return "STDENDL";
    }
}
