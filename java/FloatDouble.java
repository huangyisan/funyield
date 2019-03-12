public class FloatDouble {
    float float_num;
    double double_num;

    public FloatDouble() {
    }

    public void setFloatNum( float float_number ) {
        float_num = float_number;
    }

    public void setDoubleNum( double double_number ) {
        double_num = double_number;
    }

    public float getFloatNum() {
        System.out.println("float num is: " + float_num);
        return float_num;
    }

    public double getDoubleNum() {
        System.out.println("double num is : " + double_num);
        return double_num;
    }


    public static void main(String []args) {
        FloatDouble TheNum = new FloatDouble();

        TheNum.setFloatNum(3.14159265358979f);
        TheNum.getFloatNum();
        TheNum.setFloatNum(1113.14159265358979f);
        TheNum.getFloatNum();
        TheNum.setDoubleNum(3.14159265358979888888888888888888888d);
        TheNum.getDoubleNum();
        TheNum.setDoubleNum(13.14159265358979888888888888888888888d);
        TheNum.getDoubleNum();
        System.out.println( (float)1113.14159265358979 );
        System.out.println( (double)1113.1415926535897988888888888 );


    }


}
