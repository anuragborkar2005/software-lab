public class MStudent {
    private int id;
    private String name;
    private double marks;

    // constructor
    public MStudent(int id, String name, double marks) {
        this.id = id;
        this.name = name;
        this.marks = marks;
    }

    // getters
    public int getId() { return id; }
    public String getName() { return name; }
    public double getMarks() { return marks; }

    // setters
    public void setId(int id) { this.id = id; }
    public void setName(String name) { this.name = name; }

    public void setMarks(double marks) { this.marks = marks; }
    @Override
    public String toString() {
        return "Student{id=" + id + ", name='" + name + "', marks=" + marks + "}";
    }

    public static void main(String[] args) {
        MStudent s = new MStudent(101, "Rahul", 88.5);
        System.out.println(s);
    }
}