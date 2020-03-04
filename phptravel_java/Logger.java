import java.io.FileWriter;

public class Logger {
    String os = System.getProperty("os.name");
    String user = System.getProperty("user.name");
    private String log_path = os.equals("Mac OS X") ? "/Users/" + user + "/results.txt" : "C:/Users/Public/Documents/results.txt";
    private FileWriter write;
    boolean can_write = false;

    protected void setCan_write(){
        try {
            this.write = new FileWriter(this.log_path);
            this.can_write = true;
        }
        catch (Exception ex){
            System.out.println("Cannot write in results file  >>  CRITICAL");
        }
    }

    protected void create_result_file(){
        setCan_write();
        if (can_write){
            this.log_data("*".repeat(50) + "\n" + " ".repeat(17) + "TEST RESULTS\n" + "*".repeat(50) + "\n\n");
        }
        else {
            System.out.println("Cannot write in results file  >>  CRITICAL");
        }
    }

    protected void log_data(String text){
        try {
            this.write.append(text).append("\n");
            this.write.flush(); //??? not working
        }
        catch (Exception ex) {
            System.out.println(text + " couldn't be written to file. Error: " + ex);
        }
    }

    protected void close_result_file(){
        try {
        this.write.close();}
        catch (Exception ex){
            System.out.println("Cannot close the results file  >>  CRITICAL  >>  Error: " + ex);
        }
    }
}
