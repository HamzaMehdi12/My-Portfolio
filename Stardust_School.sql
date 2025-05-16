        -- Creating a students table with information based on EER diagram.
        -- The table has a pass value of GPA 2.0


        --The course table would generate the available courses that are to be selected by students and taught by teacher.
        --Each course is dedicated to be offered in the year or not, depeding upon class size and strength.

        CREATE TABLE Course(
            course_ID INT NOT NULL UNIQUE,
            course_name VARCHAR(20) NOT NULL UNIQUE,
            credits INT NOT NULL,
            session VARCHAR(10),
            Offered VARCHAR(1) NOT NULL,
            PRIMARY KEY(course_ID)
        );

        DROP TABLE Course;

        CREATE TABLE Teacher(
            Teacher_ID INT NOT NULL UNIQUE,
            first_name VARCHAR(20) NOT NULL,
            last_name VARCHAR(20) NOT NULL,
            email VARCHAR(20) NOT NULL UNIQUE,
            course_ID INT DEFAULT NULL,
            course_name VARCHAR(20) DEFAULT NULL,
            PRIMARY KEY(Teacher_ID),
            FOREIGN KEY(course_name) REFERENCES Course(course_name) ON DELETE CASCADE,
            FOREIGN KEY(course_ID) REFERENCES Course(course_ID) ON DELETE CASCADE
        );

        DROP TABLE Teacher;

        CREATE TABLE Student(
            std_ID INT NOT NULL UNIQUE,
            first_name VARCHAR(20) NOT NULL,
            last_name VARCHAR(20) NOT NULL,
            birth_date DATE NOT NULL,
            email VARCHAR(20) NOT NULL UNIQUE,
            Teacher_ID INT DEFAULT NULL,
            course_ID INT DEFAULT NULL,
            course_name VARCHAR(20),
            credits INT DEFAULT NULL, 
            gpa FLOAT DEFAULT NULL,
            CGPA FLOAT DEFAULT NULL,
            result VARCHAR(4) DEFAULT NULL,
            Year_ INT DEFAULT NULL,
            PRIMARY KEY(std_ID),
            FOREIGN KEY(Teacher_ID) REFERENCES Teacher(Teacher_ID) ON DELETE CASCADE,
            FOREIGN KEY(course_ID) REFERENCES Course(course_ID) ON DELETE CASCADE,
            FOREIGN KEY(course_name) REFERENCES Course(course_name) ON DELETE CASCADE
        );

        DROP TABLE Student;


        INSERT INTO Course(course_ID, course_name, credits, Session, Offered)
        VALUES
            (11002025, 'Applied Mathematics', 4, 'FALL', 'Y'),
            (11012025, 'AI', 4, 'SPRING', 'Y'),
            (11022025, 'Envirn Systems', 2, 'SPRING', 'Y'),
            (11030205, 'Control Engineerin', 4, 'FALL', 'Y'),
            (55012024, 'Electrical Engg', 4, 'SPRING', 'N'),
            (11042025, 'Discrete Math', 2, 'SPRING', 'Y'),
            (11052025, 'Linguistics', 2, 'FALL', 'Y'),
            (11062025, 'Deep Learning', 4, 'SPRING', 'Y'),
            (11072025, 'Machine Learning', 4, 'SPRING', 'N'),
            (11082025, 'LSI Design', 2, 'FALL', 'Y'),
            (11092025, 'Stats', 2, 'FALL', 'N'),
            (55022024, 'Management', 2, 'SPRING', 'N'),
            (55032024, 'Operating Sys', 4, 'FALL', 'N'),
            (49002023, 'CVT', 2, 'FALL', 'N');

        --Now entering values in Teacher column. All values are ficticious. 1 course is taught by 1 Teacher only

        INSERT INTO Teacher(Teacher_ID, first_name, last_name, email)
        VALUES
            (00110000, 'Abdul', 'Kaleem', 'abdk121@gmail.com'),
            (00110001, 'Hamza', 'Mehdi', 'smhm97@gmail.com'),#This is me ☺
            (00110002, 'Abdur', 'Rehman', 'arw98@gmail.com'),
            (00110003, 'Mark', 'Cuban', 'hworld@outlook.com'),
            (00110010, 'Andrew', 'Hamilton', 'ah1212@outlook.com'),
            (00110011, 'Shanto', 'Kaleem', 'abxsH12@gmail.com');

        UPDATE Teacher
        SET Teacher.course_ID = 11002025, Teacher.course_name = 'Applied Mathematics'
        WHERE Teacher_ID = 110000;

        UPDATE Teacher
        SET Teacher.course_ID = 11012025, Teacher.course_name = 'AI'
        WHERE Teacher.Teacher_ID = 110001;

        UPDATE Teacher
        SET Teacher.course_ID = 11030205, Teacher.course_name = 'Control Engineerin'
        WHERE Teacher.Teacher_ID = 110002;

        UPDATE Teacher
        SET Teacher.course_ID = 11062025, Teacher.course_name = 'Deep Learning'
        WHERE Teacher.Teacher_ID = 110003;

        UPDATE Teacher
        SET Teacher.course_ID = 11052025, Teacher.course_name = 'Linguistics'
        WHERE Teacher.Teacher_ID = 110010;

        UPDATE Teacher
        SET Teacher.course_ID = 11042025, Teacher.course_name = 'Discrete Math'
        WHERE Teacher.Teacher_ID = 110011;


        --Adding studnts to our list now. Multiple students can have 1 teacher.

        INSERT INTO Student(std_ID, first_name, last_name, birth_date, email)
        VALUES
            (250001, 'Wang', 'XiLing', '1997-12-19', 'wxling@gmail.com'),
            (250002, 'Sheeza', 'Sania', '1994-05-04', 'ssania@gmail.com'),
            (250003, 'Kim', 'Minseo', '1995-07-22', 'mkim@gmail.com'),
            (250004, 'Ali', 'Zara', '1998-02-14', 'zali@gmail.com'),
            (250005, 'Singh', 'Ravi', '1993-11-03', 'rsingh@gmail.com'),
            (250006, 'Gomez', 'Maria', '1992-08-19', 'mgomez@gmail.com'),
            (250007, 'Tanaka', 'Yuki', '1996-01-27', 'ytanaka@gmail.com'),
            (250008, 'Brown', 'Emma', '1994-09-30', 'ebrown@gmail.com'),
            (250009, 'Nguyen', 'Linh', '1997-05-06', 'lnguyen@gmail.com'),
            (250010, 'Khan', 'Ayaan', '1995-12-11', 'akhan@gmail.com'),
            (250011, 'Zhou', 'Mei', '1993-04-18', 'mzhou@gmail.com'),
            (250012, 'Garcia', 'Luis', '1992-06-15', 'lgarcia@gmail.com'),
            (250013, 'Patel', 'Nisha', '1996-10-20', 'npatel@gmail.com'),
            (250014, 'Lee', 'Jisoo', '1994-01-05', 'jlee@gmail.com'),
            (250015, 'Ahmed', 'Hassan', '1995-03-29', 'hahmed@gmail.com'),
            (250016, 'Smith', 'Olivia', '1997-07-12', 'osmith@gmail.com'),
            (250017, 'Choi', 'Hyun', '1993-08-25', 'hchoi@gmail.com'),
            (250018, 'Rodriguez', 'Carlos', '1991-10-17', 'crodriguez@gmail.com'),
            (250019, 'Yadav', 'Priya', '1998-04-23', 'pyadav@gmail.com'),
            (250020, 'Johnson', 'Liam', '1992-11-30', 'ljohnson@gmail.com'),
            (250021, 'Lopez', 'Ana', '1996-02-16', 'alopez@gmail.com'),
            (250022, 'Chen', 'Wei', '1994-06-21', 'wchen@gmail.com'),
            (250023, 'Fernandez', 'Diego', '1997-01-09', 'dfernandez@gmail.com'),
            (250024, 'Rossi', 'Giulia', '1995-09-13', 'grossi@gmail.com'),
            (250025, 'Kumar', 'Arjun', '1993-05-02', 'akumar@gmail.com'),
            (250026, 'Park', 'Soojin', '1998-08-08', 'spark@gmail.com'),
            (250027, 'Davies', 'Ella', '1992-03-26', 'edavies@gmail.com'),
            (250028, 'Aliyev', 'Nurlan', '1991-12-07', 'naliyev@gmail.com'),
            (250029, 'Dubois', 'Chloe', '1996-04-11', 'cdubois@gmail.com'),
            (250030, 'Rahman', 'Imran', '1994-10-01', 'irahman@gmail.com'),
            (250031, 'Petrova', 'Elena', '1993-07-19', 'epetrova@gmail.com'),
            (250032, 'Martinez', 'Juan', '1997-02-24', 'jmartinez@gmail.com'),
            (250033, 'Osei', 'Kwame', '1995-06-06', 'kosei@gmail.com'),
            (250034, 'Novak', 'Luka', '1998-09-10', 'lnovak@gmail.com'),
            (250035, 'Sato', 'Haruka', '1992-01-30', 'hsato@gmail.com'),
            (250036, 'Mueller', 'Anna', '1991-05-28', 'amueller@gmail.com'),
            (250037, 'Kimani', 'Amani', '1993-08-14', 'akimani@gmail.com'),
            (250038, 'Popescu', 'Andrei', '1994-11-08', 'apopescu@gmail.com'),
            (250039, 'Silva', 'Beatriz', '1996-03-01', 'bsilva@gmail.com'),
            (250040, 'Cohen', 'Noa', '1995-12-05', 'ncohen@gmail.com');


        --Updated Tables
        --Adding Teacher to each students. Again, Multiple students can have a single teacher

        UPDATE Student
        SET
            Teacher_ID = CASE
                WHEN std_ID BETWEEN 250001 AND 250006 THEN 110000
                WHEN std_ID BETWEEN 250007 AND 250020 THEN 110001
                WHEN std_ID BETWEEN 250021 AND 250028 THEN 110002
                WHEN std_ID BETWEEN 250029 AND 250034 THEN 110003
                WHEN std_ID BETWEEN 250035 AND 250037 THEN 110010
                WHEN std_ID BETWEEN 250038 AND 250040 THEN 110011
            END,
            course_ID = CASE
                WHEN std_ID BETWEEN 250001 AND 250006 THEN 11002025
                WHEN std_ID BETWEEN 250007 AND 250020 THEN 11012025
                WHEN std_ID BETWEEN 250021 AND 250028 THEN 11030205 
                WHEN std_ID BETWEEN 250029 AND 250034 THEN 11062025
                WHEN std_ID BETWEEN 250035 AND 250037 THEN 11052025
                WHEN std_ID BETWEEN 250038 AND 250040 THEN 11042025
            END,
            course_name = CASE
                WHEN std_ID BETWEEN 250001 AND 250006 THEN 'Applied Mathematics'
                WHEN std_ID BETWEEN 250007 AND 250020 THEN 'AI'
                WHEN std_ID BETWEEN 250021 AND 250028 THEN 'Control Engineerin'
                WHEN std_ID BETWEEN 250029 AND 250034 THEN 'Deep Learning'
                WHEN std_ID BETWEEN 250035 AND 250037 THEN 'Linguistics'
                WHEN std_ID BETWEEN 250038 AND 250040 THEN 'Discrete Math'
            END
        WHERE std_ID BETWEEN 250001 AND 250040;

        UPDATE Student
        JOIN Course AS c
            ON Student.course_ID = c.course_ID
        SET
            Student.credits = CASE
                WHEN Student.course_ID = 11002025 THEN c.credits
                WHEN Student.course_ID = 11012025 THEN c.credits
                WHEN Student.course_ID = 11030205 THEN c.credits
                WHEN Student.course_ID = 11062025 THEN c.credits
                WHEN Student.course_ID = 11052025 THEN c.credits
                WHEN Student.course_ID = 11042025 THEN c.credits
                ELSE NULL
            END
        WHERE Student.course_ID BETWEEN 11002025 AND 11062025;


        --NOW implementing the parents table




        INSERT INTO Parent(first_name, last_name)
        VALUES
            ('Amanda', 'Smith'),
        ('John',    'Doe'),
        ('Emma',    'Johnson'),
        ('Michael', 'Brown'),
        ('Olivia',  'Davis'),
        ('William', 'Miller'),
        ('Sophia',  'Wilson'),
        ('James',   'Moore'),
        ('Isabella','Taylor'),
        ('Benjamin','Anderson'),
        ('Mia',     'Thomas'),
        ('Alexander','Jackson'),
        ('Charlotte','White'),
        ('Henry',   'Harris'),
        ('Amelia',  'Martin');


        --Final View of Table.

        SELECT * FROM Course;

        SELECT * FROM Teacher;

        SELECT * FROM Student;
            




















        --BELOW IS THE PRESENTATION USING WHILE BUT DIDN'T WORK IN POPSQL. BUT IT SEEMS CORRECT

        DROP PROCEDURE IF EXISTS assign_teacher_1;

        CREATE PROCEDURE assign_teacher_1()
        BEGIN
            DECLARE i INT DEFAULT 250001;
            WHILE i <= 250006 DO
                UPDATE Student 
                SET Student.Teacher_ID = 110000, 
                    Student.course_ID = 11002025, 
                    Student.course_name = 'Applied Mathematics' 
                WHERE Student.std_ID = i;
                SET i = i + 1;
            END WHILE;
        END;

        CALL assign_teacher_1();

        CREATE PROCEDURE assign_teacher_2()
        BEGIN
            DECLARE i INT DEFAULT 250007;
            WHILE i <= 250020 DO
                UPDATE Student 
                SET Student.Teacher_ID = 110001, 
                    Student.course_ID = 11012025, 
                    Student.course_name = 'AI' 
                WHERE Student.std_ID = i;
                SET i = i + 1;
            END WHILE;
        END;

        CALL assign_teacher_2();

        CREATE PROCEDURE assign_teacher_3()
        BEGIN
            DECLARE i INT DEFAULT 250021;
            WHILE i <= 250028 DO
                UPDATE Student 
                SET Student.Teacher_ID = 110002, 
                    Student.course_ID = 11030205, 
                    Student.course_name = 'Control Engineerin' 
                WHERE Student.std_ID = i;
                SET i = i + 1;
            END WHILE;
        END;

        CALL assign_teacher_3();

        CREATE PROCEDURE assign_teacher_4()
        BEGIN
            DECLARE i INT DEFAULT 250029;
            WHILE i <= 250034 DO
                UPDATE Student 
                SET Student.Teacher_ID = 110003, 
                    Student.course_ID = 11062025, 
                    Student.course_name = 'Deep Learning' 
                WHERE Student.std_ID = i;
                SET i = i + 1;
            END WHILE;
        END;

        CALL assign_teacher_4();

        CREATE PROCEDURE assign_teacher_5()
        BEGIN
            DECLARE i INT DEFAULT 250035;
            WHILE i <= 250037 DO
                UPDATE Student SET Student.Teacher_ID = 110010, Student.course_ID = 11052025, Student.course_name = 'Linguistics' WHERE Student.std_ID = i;
                SET i = i + 1;
            END WHILE;
        END;

        CALL assign_teacher_5();

        CREATE PROCEDURE assign_teacher_6()
        BEGIN
            DECLARE i INT DEFAULT 250038;
            WHILE i <= 250040 DO
                UPDATE Student SET Student.Teacher_ID = 110011, Student.course_ID = 11042025, Student.course_name = 'Discrete Math' WHERE Student.std_ID = i;
                SET i = i + 1;
            END WHILE;
        END;

        CALL assign_teacher_6();
