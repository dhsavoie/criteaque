CREATE DATABASE criteaque;
CREATE USER 'webapp'@'%' IDENTIFIED BY 'abc123';
GRANT ALL PRIVILEGES ON criteaque.* TO 'webapp'@'%';
FLUSH PRIVILEGES;

USE criteaque;

CREATE TABLE Administrator(
    AdminID INT NOT NULL,
    FirstName VARCHAR(20) NOT NULL,
    LastName VARCHAR(20) NOT NULL,
    Username VARCHAR(20) AS (CONCAT(LastName, ".", SUBSTRING(FirstName, 1, 2))),
    Email VARCHAR(50) AS (CONCAT(Username, "@northeastern.edu")),
    Password VARCHAR(50) NOT NULL,
    PRIMARY KEY (AdminID)
);

insert into Administrator (AdminID, FirstName, LastName, Email, Username, Password) values ('07386', 'Spence', 'Antonowicz', DEFAULT, DEFAULT, 'chlwuP');
insert into Administrator (AdminID, FirstName, LastName, Email, Username, Password) values ('07023', 'Lory', 'Duffet', DEFAULT, DEFAULT, 'NaKkaejxd');
insert into Administrator (AdminID, FirstName, LastName, Email, Username, Password) values ('03560', 'Malvina', 'Rebeiro', DEFAULT, DEFAULT, 'J8EMAdpVfQ');
insert into Administrator (AdminID, FirstName, LastName, Email, Username, Password) values ('01090', 'Roby', 'Mincher', DEFAULT, DEFAULT, 'SCQzWm');
insert into Administrator (AdminID, FirstName, LastName, Email, Username, Password) values ('03031', 'Angelle', 'Schiementz', DEFAULT, DEFAULT, 'XgI8uNR1Y0');

CREATE TABLE Department(
    DepartmentName VARCHAR(50) NOT NULL,
    NumOfStudents INT NOT NULL,
    NumOfProfessors INT NOT NULL,
    PRIMARY KEY (DepartmentName)
);

insert into Department (DepartmentName, NumOfStudents, NumOfProfessors) values ('Engineering', 1935, 128);
insert into Department (DepartmentName, NumOfStudents, NumOfProfessors) values ('Business', 2143, 178);
insert into Department (DepartmentName, NumOfStudents, NumOfProfessors) values ('Health Science', 2214, 95);
insert into Department (DepartmentName, NumOfStudents, NumOfProfessors) values ('English', 1607, 149);
insert into Department (DepartmentName, NumOfStudents, NumOfProfessors) values ('History', 885, 92);

CREATE TABLE AdminDepartment(
    AdminID INT NOT NULL,
    DepartmentName VARCHAR(50) NOT NULL,
    PRIMARY KEY (AdminID, DepartmentName),
    CONSTRAINT FK_AdminDepartmentAdmin 
        FOREIGN KEY (AdminID) 
        REFERENCES Administrator(AdminID),
    CONSTRAINT FK_AdminDepartmentDepartment
        FOREIGN KEY (DepartmentName)
        REFERENCES Department(DepartmentName)
);

insert into AdminDepartment (AdminID, DepartmentName) values ('07386', 'Engineering');
insert into AdminDepartment (AdminID, DepartmentName) values ('07023', 'Business');
insert into AdminDepartment (AdminID, DepartmentName) values ('03560', 'Health Science');
insert into AdminDepartment (AdminID, DepartmentName) values ('01090', 'English');
insert into AdminDepartment (AdminID, DepartmentName) values ('03031', 'History');

CREATE TABLE Major(
    Major VARCHAR(50) NOT NULL,
    Department VARCHAR(50) NOT NULL,
    PRIMARY KEY (Major, Department),
    CONSTRAINT FK_MajorDepartment 
        FOREIGN KEY (Department) 
        REFERENCES Department(DepartmentName)
);

insert into Major (Major, Department) values ('Computer Science', 'Engineering');
insert into Major (Major, Department) values ('Electrical Engineering', 'Engineering');
insert into Major (Major, Department) values ('Mechanical Engineering', 'Engineering');
insert into Major (Major, Department) values ('Business Administration', 'Business');
insert into Major (Major, Department) values ('Health Science', 'Health Science');
insert into Major (Major, Department) values ('English', 'English');
insert into Major (Major, Department) values ('History', 'History');

-- eventually find a way to make username derived from email
CREATE TABLE Student(
    StudentID INT NOT NULL,
    FirstName VARCHAR(20) NOT NULL,
    LastName VARCHAR(20) NOT NULL,
    Username VARCHAR(20) AS (CONCAT(LastName, ".", SUBSTRING(FirstName, 1, 2))),
    Email VARCHAR(50) AS (CONCAT(Username, "@northeastern.edu")),
    Year INT,
    Password VARCHAR(50) NOT NULL,
    Major VARCHAR(50) NOT NULL,
    PRIMARY KEY (StudentID),
    CONSTRAINT FK_StudentMajor
        FOREIGN KEY (Major)
        REFERENCES Major(Major)
);

insert into Student (StudentID, FirstName, LastName, email, Year, Username, Password, Major) values ('008985560', 'Lyell', 'Goscar', DEFAULT, 2, DEFAULT, 'dIGdTj8Mg5N', 'Computer Science');
insert into Student (StudentID, FirstName, LastName, email, Year, Username, Password, Major) values ('003207531', 'Kally', 'Cornick', DEFAULT, 1, DEFAULT, 't05d26eEIqW', 'English');
insert into Student (StudentID, FirstName, LastName, email, Year, Username, Password, Major) values ('005623950', 'Annora', 'Gallagher', DEFAULT, 1, DEFAULT, 'Qre0RWyhj8', 'History');
insert into Student (StudentID, FirstName, LastName, email, Year, Username, Password, Major) values ('002505878', 'Marcie', 'Blesli', DEFAULT, 4, DEFAULT, 'tmWuT7w', 'Business Administration');
insert into Student (StudentID, FirstName, LastName, email, Year, Username, Password, Major) values ('007110349', 'Jeno', 'Huckster', DEFAULT, 4, DEFAULT, 'OvV7jngnz233', 'Mechanical Engineering');
insert into Student (StudentID, FirstName, LastName, email, Year, Username, Password, Major) values ('000851446', 'Blair', 'Cornfoot', DEFAULT, 5, DEFAULT, 'kf2dp85RJ9XA', 'Computer Science');
insert into Student (StudentID, FirstName, LastName, email, Year, Username, Password, Major) values ('002606521', 'Orlan', 'Stagg', DEFAULT, 1, DEFAULT, 'V1vI0n', 'Electrical Engineering');
insert into Student (StudentID, FirstName, LastName, email, Year, Username, Password, Major) values ('003585784', 'Melicent', 'Tarbett', DEFAULT, 1, DEFAULT, 'VzrA0k80ttM8', 'English');
insert into Student (StudentID, FirstName, LastName, email, Year, Username, Password, Major) values ('007430669', 'Hollyanne', 'Medina', DEFAULT, 3, DEFAULT, 'R5mflG4', 'Health Science');
insert into Student (StudentID, FirstName, LastName, email, Year, Username, Password, Major) values ('008692645', 'Lexi', 'Sherland', DEFAULT, 3, DEFAULT, '2GH3RLs2', 'History');

CREATE TABLE Professor(
    ProfessorID INT NOT NULL,
    FirstName VARCHAR(20) NOT NULL,
    LastName VARCHAR(20) NOT NULL,
    Username VARCHAR(20) AS (CONCAT(LastName, ".", SUBSTRING(FirstName, 1, 2))),
    Email VARCHAR(50) AS (CONCAT(Username, "@northeastern.edu")),
    Password VARCHAR(50) NOT NULL,
    Tenured BOOLEAN NOT NULL,
    SchoolAttended VARCHAR(50) NOT NULL,
    HighestDegree VARCHAR(50) NOT NULL,
    YearsTaught INT NOT NULL,
    Department VARCHAR(50) NOT NULL,
    PRIMARY KEY (ProfessorID),
    CONSTRAINT FK_ProfessorDepartment
        FOREIGN KEY (Department)
        REFERENCES Department(DepartmentName)
);

insert into Professor (ProfessorID, FirstName, LastName, email, Username, Password, Tenured, SchoolAttended, HighestDegree, YearsTaught, Department) values ('000827368', 'Isaiah', 'Adamowitz', DEFAULT, DEFAULT, 'GSQ4WrHKlzZ', false, 'Fordham University', 'Masters', 22, 'Health Science');
insert into Professor (ProfessorID, FirstName, LastName, email, Username, Password, Tenured, SchoolAttended, HighestDegree, YearsTaught, Department) values ('008360583', 'Norry', 'Bassick', DEFAULT, DEFAULT, 'CN7D1SAeNLH', true, 'Universidad Andina Simón Bolivar', 'Masters', 10, 'Engineering');
insert into Professor (ProfessorID, FirstName, LastName, email, Username, Password, Tenured, SchoolAttended, HighestDegree, YearsTaught, Department) values ('008195942', 'Humfrid', 'Clemo', DEFAULT, DEFAULT, 'qMBVAb2mo', true, 'The Art Institutes International Portland', 'PhD', 10, 'Business');
insert into Professor (ProfessorID, FirstName, LastName, email, Username, Password, Tenured, SchoolAttended, HighestDegree, YearsTaught, Department) values ('007418475', 'Meggy', 'Spinks', DEFAULT, DEFAULT, 'Ip5idMAoTsCK', true, 'Hochschule Bremen', 'PhD', 8, 'Business');
insert into Professor (ProfessorID, FirstName, LastName, email, Username, Password, Tenured, SchoolAttended, HighestDegree, YearsTaught, Department) values ('008591029', 'Kath', 'Hardy-Piggin', DEFAULT, DEFAULT, 'ZiZtoEgPjRd', false, 'KDU College Sdn Bhd', 'PhD', 29, 'Health Science');

CREATE TABLE Course(
    CourseSection VARCHAR(10) NOT NULL,
    CourseName VARCHAR(50) NOT NULL,
    Professor INT NOT NULL,
    PRIMARY KEY (CourseSection, Professor),
    CONSTRAINT CourseProfessor 
        FOREIGN KEY (Professor) 
        REFERENCES Professor(ProfessorID)
);


insert into Course (CourseSection, CourseName, Professor) values ('HS1000', 'Introduction to Health Science', '000827368');
insert into Course (CourseSection, CourseName, Professor) values ('CS2560', 'Introduction to Machine Learning', '008360583');
insert into Course (CourseSection, CourseName, Professor) values ('B1600', 'The art of Business', '008195942');
insert into Course (CourseSection, CourseName, Professor) values ('B2700', 'Intermediate Market Analysis', '007418475');
insert into Course (CourseSection, CourseName, Professor) values ('HS1500', 'Anatomy and Physiology', '008591029');

CREATE TABLE ComparisonSide1(
    ComparisonID INT NOT NULL PRIMARY KEY,
    ProfessorID INT NOT NULL,
    CONSTRAINT FK_ComparisonSide1Professor 
        FOREIGN KEY (ProfessorID) 
        REFERENCES Professor (ProfessorID)
        ON UPDATE cascade ON DELETE restrict
);

insert into ComparisonSide1 (ComparisonID, ProfessorID) values (1, '000827368');
insert into ComparisonSide1 (ComparisonID, ProfessorID) values (2, '008360583');
insert into ComparisonSide1 (ComparisonID, ProfessorID) values (3, '008195942');

CREATE TABLE ComparisonSide2(
    ComparisonID INT NOT NULL PRIMARY KEY,
    Professor INT NOT NULL,
    CONSTRAINT FK_ComparisonSide2Professor 
        FOREIGN KEY (Professor) 
        REFERENCES Professor (ProfessorID)
        ON UPDATE cascade ON DELETE restrict,
    CONSTRAINT FK_Comparisons
        FOREIGN KEY (ComparisonID)
        REFERENCES ComparisonSide1(ComparisonID)
        ON UPDATE cascade ON DELETE restrict
);

insert into ComparisonSide2 (ComparisonID, Professor) values (1, '008360583');
insert into ComparisonSide2 (ComparisonID, Professor) values (2, '008195942');
insert into ComparisonSide2 (ComparisonID, Professor) values (3, '007418475');

-- figure out how to make overall derived from the other 3
CREATE TABLE Review (
    ReviewID INT NOT NULL,
    Upvotes INT NOT NULL,
    Downvotes INT NOT NULL,
    ReviewContent VARCHAR(500) NOT NULL,
    DateCreated DATETIME DEFAULT CURRENT_TIMESTAMP,
    DateModified DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    Class VARCHAR(10) NOT NULL,
    WorkloadRating INT NOT NULL,
    DifficultyRating INT NOT NULL,
    EngagementRating INT NOT NULL,
    OverallRating INT NOT NULL,
    StudentReviewer INT NOT NULL,
    ProfessorReviewed INT NOT NULL,
    PRIMARY KEY (ReviewID),
    CONSTRAINT FK_StudentReviewer 
        FOREIGN KEY (StudentReviewer) 
        REFERENCES Student (StudentID) 
        ON UPDATE cascade ON DELETE restrict,
    CONSTRAINT FK_ProfessorReviewed 
        FOREIGN KEY (ProfessorReviewed) 
        REFERENCES Professor (ProfessorID) 
        ON UPDATE cascade ON DELETE restrict
);

insert into Review (ReviewID, Upvotes, Downvotes, ReviewContent, Class, WorkloadRating, DifficultyRating, EngagementRating, OverallRating, StudentReviewer, ProfessorReviewed) values (1, 0, 0, 'This class was very interesting and the professor was very engaging. I would recommend this class to anyone who is interested in health science.', 'HS1000', 3, 2, 4, 3, '007430669', '000827368');
insert into Review (ReviewID, Upvotes, Downvotes, ReviewContent, Class, WorkloadRating, DifficultyRating, EngagementRating, OverallRating, StudentReviewer, ProfessorReviewed) values (2, 0, 0, 'This class was quite difficult and had a heavy workload, but the professor was very engaging.', 'HS1000', 4, 4, 4, 4, '007430669', '000827368');

CREATE TABLE Approval(
    DateApproved DATETIME DEFAULT CURRENT_TIMESTAMP,
    ApprovingAdminID INT NOT NULL,
    Reasoning VARCHAR(500) NOT NULL,
    ReviewID INT NOT NULL,
    CONSTRAINT FK_ApprovingAdminID 
        FOREIGN KEY (ApprovingAdminID) 
        REFERENCES Administrator (AdminID)
        ON UPDATE cascade ON DELETE restrict,
    CONSTRAINT FK_ReviewID
        FOREIGN KEY (ReviewID)
        REFERENCES Review(ReviewID)
        ON UPDATE cascade ON DELETE restrict
);

insert into Approval (DateApproved, ApprovingAdminID, Reasoning, ReviewID) values ('2020-11-20 00:00:00', '07023', 'This review is very well written and is a good representation of the professor.', 1);
insert into Approval (DateApproved, ApprovingAdminID, Reasoning, ReviewID) values ('2020-11-20 00:00:00', '07386', 'This review is very well written and is a good representation of the professor.', 2);
