import sqlite3

conn = sqlite3.connect('kansas_mart.db')
cursor = conn.cursor()

# Create tables
cursor.executescript("""
CREATE TABLE Suppliers (
    SupplierID INTEGER PRIMARY KEY,
    SupplierName TEXT,
    ContactInfo TEXT
);

CREATE TABLE Products (
    ProductID INTEGER PRIMARY KEY,
    Name TEXT,
    Description TEXT,
    Price REAL,
    StockQuantity INTEGER,
    SupplierID INTEGER,
    FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID)
);

CREATE TABLE Customers (
    CustomerID INTEGER PRIMARY KEY,
    FirstName TEXT,
    LastName TEXT,
    Email TEXT,
    PhoneNumber TEXT,
    Address TEXT
);

CREATE TABLE Orders (
    OrderID INTEGER PRIMARY KEY,
    CustomerID INTEGER,
    OrderDate TEXT,
    TotalAmount REAL,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

CREATE TABLE OrderItems (
    OrderItemID INTEGER PRIMARY KEY,
    OrderID INTEGER,
    ProductID INTEGER,
    Quantity INTEGER,
    UnitPrice REAL,
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);
""")

# Insert sample data
cursor.executescript("""
INSERT INTO Suppliers VALUES (1, 'Fresh Farms', 'freshfarms@email.com');
INSERT INTO Suppliers VALUES (2, 'Green Harvest', 'greenharvest@email.com');
INSERT INTO Suppliers VALUES (3, 'Popular Farms', 'popularfarms@email.com');
INSERT INTO Suppliers VALUES (4, 'Yellow Harvest', 'yellowharvest@email.com');

INSERT INTO Products VALUES (101, 'Apples', 'Red apples', 2.50, 100, 1);
INSERT INTO Products VALUES (102, 'Bananas', 'Yellow bananas', 1.20, 150, 2);
INSERT INTO Products VALUES (103, 'Carrots', 'Fresh carrots', 0.80, 900, 3);
INSERT INTO Products VALUES (104, 'Pineapple', 'Brown pineapple', 0.94, 600, 4);
INSERT INTO Products VALUES (105, 'Tomatoes', 'Red tomatoes', 1.50, 200, 2);
INSERT INTO Products VALUES (106, 'Lettuce', 'Green lettuce', 1.10, 75, 3);
INSERT INTO Products VALUES (107, 'Oranges', 'Sweet oranges', 1.40, 180, 1);
INSERT INTO Products VALUES (108, 'Cabbage', 'Fresh green cabbage', 1.30, 60, 2);

INSERT INTO Customers VALUES (201, 'John', 'Doe', 'john@email.com', '111-222-3333', '123 Main St');
INSERT INTO Customers VALUES (202, 'Jane', 'Smith', 'jane@email.com', '222-333-4444', '456 Oak St');
INSERT INTO Customers VALUES (203, 'Robert', 'Philips', 'robp@email.com', '111-888-3333', '129 Main St');
INSERT INTO Customers VALUES (204, 'Steve', 'Smith', 'steve@email.com', '222-999-4444', '406 Oak St');
INSERT INTO Customers VALUES (205, 'Emily', 'Stone', 'emily@email.com', '333-222-1111', '789 Pine St');
INSERT INTO Customers VALUES (206, 'Mike', 'Brown', 'mike@email.com', '555-444-2222', '654 Cedar St');

INSERT INTO Orders VALUES (301, 201, '2025-03-29', 6.80);
INSERT INTO Orders VALUES (302, 202, '2025-03-30', 3.60);
INSERT INTO Orders VALUES (303, 203, '2025-03-29', 7.80);
INSERT INTO Orders VALUES (304, 204, '2025-03-30', 9.60);
INSERT INTO Orders VALUES (305, 205, '2025-03-30', 4.30);

INSERT INTO OrderItems VALUES (401, 301, 101, 2, 2.50); 
INSERT INTO OrderItems VALUES (402, 301, 103, 2, 0.90); 
INSERT INTO OrderItems VALUES (403, 302, 102, 3, 1.20); 
INSERT INTO OrderItems VALUES (404, 303, 104, 4, 1.90); 
INSERT INTO OrderItems VALUES (405, 304, 105, 3, 1.50);
INSERT INTO OrderItems VALUES (406, 305, 106, 2, 1.10);
INSERT INTO OrderItems VALUES (407, 305, 107, 1, 1.40);
""")

conn.commit()
conn.close()

print("SQLite database created and populated successfully!")
