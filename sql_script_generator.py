def main():
    script_output()


createTable = {"SQL Server":
               """
    CREATE TABLE TestTable (
        BusinessEntityID INT NOT NULL,
        PersonType NCHAR(2) NOT NULL,
        Title NVARCHAR(8) NULL,
        FirstName NVARCHAR(50) NOT NULL,
        MiddleName NVARCHAR(50) NULL,
        LastName NVARCHAR(50) NOT NULL,
        Suffix NVARCHAR(10) NULL,
        EmailPromotion INT NOT NULL,
        AdditionalContactInfo XML NULL,
        Demographics XML NULL,
        rowguid UNIQUEIDENTIFIER  NOT NULL,
        ModifiedDate DATETIME NOT NULL
	)
	
    INSERT INTO TestTable
    VALUES(1, 'EM', 'Ms.', 'Aretha', 'Louise', 'Franklin', NULL, 0, NULL, '<IndividualSurvey xmlns="http://schemas. microsoft.com/sqlserver/2004/07/adventure-works/IndividualSurvey"><TotalPurchaseYTD>0</TotalPurchaseYTD></IndividualSurvey>', '92C4279F-1207-48A3-8448-4636514EB7E2', '2009-01-07 00:00:00.000'),
        (2, 'EM', 'Mr.', 'Robert', 'Leroy', 'Johnson', NULL, 0, NULL, '<IndividualSurvey xmlns="http://schemas.microsoft.com/sqlserver/2004/07/adventure-works/IndividualSurvey"><TotalPurchaseYTD>0</TotalPurchaseYTD></IndividualSurvey>', '92C4279F-1207-48A3-8448-4636514EB7E3', '2009-01-08 00:00:00.000'),
        (3, 'EM', 'Ms.', 'Janis', 'Lyn', 'Joplin', NULL, 0, NULL, '<IndividualSurvey xmlns="http://schemas.microsoft.com/sqlserver/2004/07/adventure-works/IndividualSurvey"><TotalPurchaseYTD>0</TotalPurchaseYTD></IndividualSurvey>', '92C4279F-1207-48A3-8448-4636514EB7E4', '2009-01-10 00:00:00.000'),
        (4, 'EM', 'Mr.', 'John', 'Winston', 'Lennon', NULL, 0, NULL, '<IndividualSurvey xmlns="http://schemas.microsoft.com/sqlserver/2004/07/adventure-works/IndividualSurvey"><TotalPurchaseYTD>0</TotalPurchaseYTD></IndividualSurvey>', '92C4279F-1207-48A3-8448-4636514EB7E5', '2009-01-11 00:00:00.000'),
        (5, 'EM', 'Ms.', 'Billie', 'Lady Day', 'Holiday', NULL, 0, NULL, '<IndividualSurvey xmlns="http://schemas.microsoft.com/sqlserver/2004/07/adventure-works/IndividualSurvey"><TotalPurchaseYTD>0</TotalPurchaseYTD></IndividualSurvey>', '92C4279F-1207-48A3-8448-4636514EB7E6', '2009-01-13 00:00:00.000'),
        (6, 'EM', 'Mr.', 'Borislav', 'V', 'Pekic', NULL, 0, NULL, '<IndividualSurvey xmlns="http://schemas.microsoft.com/sqlserver/2004/07/adventure-works/IndividualSurvey"><TotalPurchaseYTD>0</TotalPurchaseYTD></IndividualSurvey>', '92C4279F-1207-48A3-8448-4636514EB7E7', '2009-01-14 00:00:00.000'),
        (7, 'EM', 'Mr.', 'Harold', 'Stage', 'Pinter', NULL, 0, NULL, '<IndividualSurvey xmlns="http://schemas.microsoft.com/sqlserver/2004/07/adventure-works/IndividualSurvey"><TotalPurchaseYTD>0</TotalPurchaseYTD></IndividualSurvey>', '92C4279F-1207-48A3-8448-4636514EB7E8', '2009-01-15 00:00:00.000'),
        (8, 'EM', 'Mr.', 'Stojan', 'Steve', 'Teshic', NULL, 0, NULL, '<IndividualSurvey xmlns="http://schemas.microsoft.com/sqlserver/2004/07/adventure-works/IndividualSurvey"><TotalPurchaseYTD>0</TotalPurchaseYTD></IndividualSurvey>', '92C4279F-1207-48A3-8448-4636514EB7E9', '2009-01-16 00:00:00.000'),
        (9, 'EM', 'Ms.', 'Mary', 'Wollstonecraft', 'Shelley', NULL, 0, NULL, '<IndividualSurvey xmlns="http://schemas.microsoft.com/sqlserver/2004/07/adventure-works/IndividualSurvey"><TotalPurchaseYTD>0</TotalPurchaseYTD></IndividualSurvey>', '92C4279F-1207-48A3-8448-4636514EB7E1', '2009-01-17 00:00:00.000'),
        (10, 'EM', 'Mr.', 'William', 'Poet', 'Blake', NULL, 0, NULL, '<IndividualSurvey xmlns="http://schemas.microsoft.com/sqlserver/2004/07/adventure-works/IndividualSurvey"><TotalPurchaseYTD>0</TotalPurchaseYTD></IndividualSurvey>', '92C4279F-1207-48A3-8448-4636514EB7D2', '2009-01-18 00:00:00.000')
    """,
               "DB2 LUW":
               """
    CREATE TABLE TestTable (
        BusinessEntityID integer NOT NULL,
        PersonType char(2) NOT NULL,
        Title varchar(8) NULL,
        FirstName varchar(50) NOT NULL,
        MiddleName varchar(50) NULL,
        LastName varchar(50) NOT NULL,
        Suffix varchar(10) NULL,
        EmailPromotion integer NOT NULL,
        AdditionalContactInfo xml NULL,
        Demographics xml NULL,
        rowguid varchar NOT NULL,
        ModifiedDate timestamp NOT NULL
    );
    INSERT INTO TestTable
    VALUES (
    1, 
    'EM', 
    'Ms.', 
    'Aretha', 
    'Louise', 
    'Franklin', 
    NULL, 
    0, 
    NULL, 
    '<IndividualSurvey xmlns="http://schemas.microsoft.com/sqlserver/2004/07/adventure-works/IndividualSurvey"><TotalPurchaseYTD>0</TotalPurchaseYTD></IndividualSurvey>', 
    '92C4279F-1207-48A3-8448-4636514EB7E2', 
    '2009-01-07 00:00:00.000'
    ), (
    2, 
    'EM', 
    'Mr.', 
    'Robert', 
    'Leroy', 
    'Johnson', 
    NULL, 
    0, 
    NULL, 
    '<IndividualSurvey xmlns="http://schemas.microsoft.com/sqlserver/2004/07/adventure-works/IndividualSurvey"><TotalPurchaseYTD>0</TotalPurchaseYTD></IndividualSurvey>', 
    '92C4279F-1207-48A3-8448-4636514EB7E3', 
    '2009-01-08 00:00:00.000'
    ), (
    3, 
    'EM', 
    'Ms.', 
    'Janis', 
    'Lyn', 
    'Joplin', 
    NULL, 
    0, 
    NULL, 
    '<IndividualSurvey xmlns="http://schemas.microsoft.com/sqlserver/2004/07/adventure-works/IndividualSurvey"><TotalPurchaseYTD>0</TotalPurchaseYTD></IndividualSurvey>', 
    '92C4279F-1207-48A3-8448-4636514EB7E4', 
    '2009-01-10 00:00:00.000'
    ), (
    4, 
    'EM', 
    'Mr.', 
    'John', 
    'Winston', 
    'Lennon', 
    NULL, 
    0, 
    NULL, 
    '<IndividualSurvey xmlns="http://schemas.microsoft.com/sqlserver/2004/07/adventure-works/IndividualSurvey"><TotalPurchaseYTD>0</TotalPurchaseYTD></IndividualSurvey>', 
    '92C4279F-1207-48A3-8448-4636514EB7E5', 
    '2009-01-11 00:00:00.000'
    ), (
    5, 
    'EM', 
    'Ms.', 
    'Billie', 
    'Lady Day', 
    'Holiday', 
    NULL, 
    0, 
    NULL, 
    '<IndividualSurvey xmlns="http://schemas.microsoft.com/sqlserver/2004/07/adventure-works/IndividualSurvey"><TotalPurchaseYTD>0</TotalPurchaseYTD></IndividualSurvey>', 
    '92C4279F-1207-48A3-8448-4636514EB7E6', 
    '2009-01-13 00:00:00.000'
    ), (
    6, 
    'EM', 
    'Mr.', 
    'Borislav', 
    'V', 
    'Pekic', 
    NULL, 
    0, 
    NULL, 
    '<IndividualSurvey xmlns="http://schemas.microsoft.com/sqlserver/2004/07/adventure-works/IndividualSurvey"><TotalPurchaseYTD>0</TotalPurchaseYTD></IndividualSurvey>', 
    '92C4279F-1207-48A3-8448-4636514EB7E7', 
    '2009-01-14 00:00:00.000'
    ), (
    7, 
    'EM', 
    'Mr.', 
    'Harold', 
    'Stage', 
    'Pinter', 
    NULL, 
    0, 
    NULL, 
    '<IndividualSurvey xmlns="http://schemas.microsoft.com/sqlserver/2004/07/adventure-works/IndividualSurvey"><TotalPurchaseYTD>0</TotalPurchaseYTD></IndividualSurvey>', 
    '92C4279F-1207-48A3-8448-4636514EB7E8', 
    '2009-01-15 00:00:00.000'
    ), (
    8, 
    'EM', 
    'Mr.', 
    'Stojan', 
    'Steve', 
    'Teshic', 
    NULL, 
    0, 
    NULL, 
    '<IndividualSurvey xmlns="http://schemas.microsoft.com/sqlserver/2004/07/adventure-works/IndividualSurvey"><TotalPurchaseYTD>0</TotalPurchaseYTD></IndividualSurvey>', 
    '92C4279F-1207-48A3-8448-4636514EB7E9', 
    '2009-01-16 00:00:00.000'
    ), (
    9, 
    'EM', 
    'Ms.', 
    'Mary', 
    'Wollstonecraft', 
    'Shelley', 
    NULL, 
    0, 
    NULL, 
    '<IndividualSurvey xmlns="http://schemas.microsoft.com/sqlserver/2004/07/adventure-works/IndividualSurvey"><TotalPurchaseYTD>0</TotalPurchaseYTD></IndividualSurvey>', 
    '92C4279F-1207-48A3-8448-4636514EB7E1', 
    '2009-01-17 00:00:00.000'
    ), (
    10, 
    'EM', 
    'Mr.', 
    'William', 
    'Poet', 
    'Blake', 
    NULL, 
    0, 
    NULL, 
    '<IndividualSurvey xmlns="http://schemas.microsoft.com/sqlserver/2004/07/adventure-works/IndividualSurvey"><TotalPurchaseYTD>0</TotalPurchaseYTD></IndividualSurvey>', 
    '92C4279F-1207-48A3-8448-4636514EB7D2', 
    '2009-01-18 00:00:00.000'
    );
    """,
               "Oracle":
               """
    CREATE TABLE TestTable (
        BusinessEntityID number(10) NOT NULL,
        PersonType nchar(2) NOT NULL,
        Title nvarchar2(8) NULL,
        FirstName nvarchar2(50) NOT NULL,
        MiddleName nvarchar2(50) NULL,
        LastName nvarchar2(50) NOT NULL,
        Suffix nvarchar2(10) NULL,
        EmailPromotion number(10) NOT NULL,
        AdditionalContactInfo xmltype NULL,
        Demographics xmltype NULL,
        rowguid varchar2 NOT NULL,
        ModifiedDate timestamp NOT NULL
    );

    INSERT INTO TestTable
    SELECT
    1,
    'EM',
    'Ms.',
    'Aretha',
    'Louise',
    'Franklin',
    NULL,
    0,
    NULL,
    '<IndividualSurvey xmlns="http://schemas.microsoft.com/sqlserver/2004/07/adventure-works/IndividualSurvey"><TotalPurchaseYTD>0</TotalPurchaseYTD></IndividualSurvey>',
    '92C4279F-1207-48A3-8448-4636514EB7E2',
    '2009-01-07 00:00:00.000'
    FROM DUAL
    UNION ALL
    SELECT
    2,
    'EM',
    'Mr.',
    'Robert',
    'Leroy',
    'Johnson',
    NULL,
    0,
    NULL,
    '<IndividualSurvey xmlns="http://schemas.microsoft.com/sqlserver/2004/07/adventure-works/IndividualSurvey"><TotalPurchaseYTD>0</TotalPurchaseYTD></IndividualSurvey>',
    '92C4279F-1207-48A3-8448-4636514EB7E3',
    '2009-01-08 00:00:00.000'
    FROM DUAL
    UNION ALL
    SELECT
    3,
    'EM',
    'Ms.',
    'Janis',
    'Lyn',
    'Joplin',
    NULL,
    0,
    NULL,
    '<IndividualSurvey xmlns="http://schemas.microsoft.com/sqlserver/2004/07/adventure-works/IndividualSurvey"><TotalPurchaseYTD>0</TotalPurchaseYTD></IndividualSurvey>',
    '92C4279F-1207-48A3-8448-4636514EB7E4',
    '2009-01-10 00:00:00.000'
    FROM DUAL
    UNION ALL
    SELECT
    4,
    'EM',
    'Mr.',
    'John',
    'Winston',
    'Lennon',
    NULL,
    0,
    NULL,
    '<IndividualSurvey xmlns="http://schemas.microsoft.com/sqlserver/2004/07/adventure-works/IndividualSurvey"><TotalPurchaseYTD>0</TotalPurchaseYTD></IndividualSurvey>',
    '92C4279F-1207-48A3-8448-4636514EB7E5',
    '2009-01-11 00:00:00.000'
    FROM DUAL
    UNION ALL
    SELECT
    5,
    'EM',
    'Ms.',
    'Billie',
    'Lady Day',
    'Holiday',
    NULL,
    0,
    NULL,
    '<IndividualSurvey xmlns="http://schemas.microsoft.com/sqlserver/2004/07/adventure-works/IndividualSurvey"><TotalPurchaseYTD>0</TotalPurchaseYTD></IndividualSurvey>',
    '92C4279F-1207-48A3-8448-4636514EB7E6',
    '2009-01-13 00:00:00.000'
    FROM DUAL
    UNION ALL
    SELECT
    6,
    'EM',
    'Mr.',
    'Borislav',
    'V',
    'Pekic',
    NULL,
    0,
    NULL,
    '<IndividualSurvey xmlns="http://schemas.microsoft.com/sqlserver/2004/07/adventure-works/IndividualSurvey"><TotalPurchaseYTD>0</TotalPurchaseYTD></IndividualSurvey>',
    '92C4279F-1207-48A3-8448-4636514EB7E7',
    '2009-01-14 00:00:00.000'
    FROM DUAL
    UNION ALL
    SELECT
    7,
    'EM',
    'Mr.',
    'Harold',
    'Stage',
    'Pinter',
    NULL,
    0,
    NULL,
    '<IndividualSurvey xmlns="http://schemas.microsoft.com/sqlserver/2004/07/adventure-works/IndividualSurvey"><TotalPurchaseYTD>0</TotalPurchaseYTD></IndividualSurvey>',
    '92C4279F-1207-48A3-8448-4636514EB7E8',
    '2009-01-15 00:00:00.000'
    FROM DUAL
    UNION ALL
    SELECT
    8,
    'EM',
    'Mr.',
    'Stojan',
    'Steve',
    'Teshic',
    NULL,
    0,
    NULL,
    '<IndividualSurvey xmlns="http://schemas.microsoft.com/sqlserver/2004/07/adventure-works/IndividualSurvey"><TotalPurchaseYTD>0</TotalPurchaseYTD></IndividualSurvey>',
    '92C4279F-1207-48A3-8448-4636514EB7E9',
    '2009-01-16 00:00:00.000'
    FROM DUAL
    UNION ALL
    SELECT
    9,
    'EM',
    'Ms.',
    'Mary',
    'Wollstonecraft',
    'Shelley',
    NULL,
    0,
    NULL,
    '<IndividualSurvey xmlns="http://schemas.microsoft.com/sqlserver/2004/07/adventure-works/IndividualSurvey"><TotalPurchaseYTD>0</TotalPurchaseYTD></IndividualSurvey>',
    '92C4279F-1207-48A3-8448-4636514EB7E1',
    '2009-01-17 00:00:00.000'
    FROM DUAL
    UNION ALL
    SELECT
    10,
    'EM',
    'Mr.',
    'William',
    'Poet',
    'Blake',
    NULL,
    0,
    NULL,
    '<IndividualSurvey xmlns="http://schemas.microsoft.com/sqlserver/2004/07/adventure-works/IndividualSurvey"><TotalPurchaseYTD>0</TotalPurchaseYTD></IndividualSurvey>',
    '92C4279F-1207-48A3-8448-4636514EB7D2',
    '2009-01-18 00:00:00.000'
    FROM DUAL;
    """,
               "MySQL":
               """
    CREATE TABLE TestTable (
        BusinessEntityID int NOT NULL,
        PersonType char(2) NOT NULL,
        Title varchar(8) NULL,
        FirstName varchar(50) NOT NULL,
        MiddleName varchar(50) NULL,
        LastName varchar(50) NOT NULL,
        Suffix varchar(10) NULL,
        EmailPromotion int NOT NULL,
        AdditionalContactInfo xml NULL,
        Demographics xml NULL,
        rowguid varchar(36) NOT NULL,
        ModifiedDate timestamp NOT NULL
    );

    INSERT INTO TestTable
    VALUES (
    1, 
    'EM', 
    'Ms.', 
    'Aretha', 
    'Louise', 
    'Franklin', 
    NULL, 
    0, 
    NULL, 
    '<IndividualSurvey xmlns="http://schemas.microsoft.com/sqlserver/2004/07/adventure-works/IndividualSurvey"><TotalPurchaseYTD>0</TotalPurchaseYTD></IndividualSurvey>', 
    '92C4279F-1207-48A3-8448-4636514EB7E2', 
    '2009-01-07 00:00:00.000'
    ), (
    2, 
    'EM', 
    'Mr.', 
    'Robert', 
    'Leroy', 
    'Johnson', 
    NULL, 
    0, 
    NULL, 
    '<IndividualSurvey xmlns="http://schemas.microsoft.com/sqlserver/2004/07/adventure-works/IndividualSurvey"><TotalPurchaseYTD>0</TotalPurchaseYTD></IndividualSurvey>', 
    '92C4279F-1207-48A3-8448-4636514EB7E3', 
    '2009-01-08 00:00:00.000'
    ), (
    3, 
    'EM', 
    'Ms.', 
    'Janis', 
    'Lyn', 
    'Joplin', 
    NULL, 
    0, 
    NULL, 
    '<IndividualSurvey xmlns="http://schemas.microsoft.com/sqlserver/2004/07/adventure-works/IndividualSurvey"><TotalPurchaseYTD>0</TotalPurchaseYTD></IndividualSurvey>', 
    '92C4279F-1207-48A3-8448-4636514EB7E4', 
    '2009-01-10 00:00:00.000'
    ), (
    4, 
    'EM', 
    'Mr.', 
    'John', 
    'Winston', 
    'Lennon', 
    NULL, 
    0, 
    NULL, 
    '<IndividualSurvey xmlns="http://schemas.microsoft.com/sqlserver/2004/07/adventure-works/IndividualSurvey"><TotalPurchaseYTD>0</TotalPurchaseYTD></IndividualSurvey>', 
    '92C4279F-1207-48A3-8448-4636514EB7E5', 
    '2009-01-11 00:00:00.000'
    ), (
    5, 
    'EM', 
    'Ms.', 
    'Billie', 
    'Lady Day', 
    'Holiday', 
    NULL, 
    0, 
    NULL, 
    '<IndividualSurvey xmlns="http://schemas.microsoft.com/sqlserver/2004/07/adventure-works/IndividualSurvey"><TotalPurchaseYTD>0</TotalPurchaseYTD></IndividualSurvey>', 
    '92C4279F-1207-48A3-8448-4636514EB7E6', 
    '2009-01-13 00:00:00.000'
    ), (
    6, 
    'EM', 
    'Mr.', 
    'Borislav', 
    'V', 
    'Pekic', 
    NULL, 
    0, 
    NULL, 
    '<IndividualSurvey xmlns="http://schemas.microsoft.com/sqlserver/2004/07/adventure-works/IndividualSurvey"><TotalPurchaseYTD>0</TotalPurchaseYTD></IndividualSurvey>', 
    '92C4279F-1207-48A3-8448-4636514EB7E7', 
    '2009-01-14 00:00:00.000'
    ), (
    7, 
    'EM', 
    'Mr.', 
    'Harold', 
    'Stage', 
    'Pinter', 
    NULL, 
    0, 
    NULL, 
    '<IndividualSurvey xmlns="http://schemas.microsoft.com/sqlserver/2004/07/adventure-works/IndividualSurvey"><TotalPurchaseYTD>0</TotalPurchaseYTD></IndividualSurvey>', 
    '92C4279F-1207-48A3-8448-4636514EB7E8', 
    '2009-01-15 00:00:00.000'
    ), (
    8, 
    'EM', 
    'Mr.', 
    'Stojan', 
    'Steve', 
    'Teshic', 
    NULL, 
    0, 
    NULL, 
    '<IndividualSurvey xmlns="http://schemas.microsoft.com/sqlserver/2004/07/adventure-works/IndividualSurvey"><TotalPurchaseYTD>0</TotalPurchaseYTD></IndividualSurvey>', 
    '92C4279F-1207-48A3-8448-4636514EB7E9', 
    '2009-01-16 00:00:00.000'
    ), (
    9, 
    'EM', 
    'Ms.', 
    'Mary', 
    'Wollstonecraft', 
    'Shelley', 
    NULL, 
    0, 
    NULL, 
    '<IndividualSurvey xmlns="http://schemas.microsoft.com/sqlserver/2004/07/adventure-works/IndividualSurvey"><TotalPurchaseYTD>0</TotalPurchaseYTD></IndividualSurvey>', 
    '92C4279F-1207-48A3-8448-4636514EB7E1', 
    '2009-01-17 00:00:00.000'
    ), (
    10, 
    'EM', 
    'Mr.', 
    'William', 
    'Poet', 
    'Blake', 
    NULL, 
    0, 
    NULL, 
    '<IndividualSurvey xmlns="http://schemas.microsoft.com/sqlserver/2004/07/adventure-works/IndividualSurvey"><TotalPurchaseYTD>0</TotalPurchaseYTD></IndividualSurvey>', 
    '92C4279F-1207-48A3-8448-4636514EB7D2', 
    '2009-01-18 00:00:00.000'
);
    """,
               "Teradata":
               """
    CREATE TABLE TestTable (
        BusinessEntityID integer NOT NULL,
        PersonType char(2) NOT NULL,
        Title varchar(8) NULL,
        FirstName varchar(50) NOT NULL,
        MiddleName varchar(50) NULL,
        LastName varchar(50) NOT NULL,
        Suffix varchar(10) NULL,
        EmailPromotion integer NOT NULL,
        AdditionalContactInfo xml NULL,
        Demographics xml NULL,
        rowguid varchar NOT NULL,
        ModifiedDate timestamp NOT NULL
    );

    INSERT INTO TestTable
    SELECT
    "t"."v0",
    "t"."v1",
    "t"."v2",
    "t"."v3",
    "t"."v4",
    "t"."v5",
    "t"."v6",
    "t"."v7",
    "t"."v8",
    "t"."v9",
    "t"."v10",
    "t"."v11"
    FROM (
    SELECT
        1,
        'EM',
        'Ms.',
        'Aretha',
        'Louise',
        'Franklin',
        NULL,
        0,
        NULL,
        '<IndividualSurvey xmlns="http://schemas.microsoft.com/sqlserver/2004/07/adventure-works/IndividualSurvey"><TotalPurchaseYTD>0</TotalPurchaseYTD></IndividualSurvey>',
        '92C4279F-1207-48A3-8448-4636514EB7E2',
        '2009-01-07 00:00:00.000'
    FROM (
        SELECT 1 AS "dual"
    ) AS "dual"
    UNION ALL
    SELECT
        2,
        'EM',
        'Mr.',
        'Robert',
        'Leroy',
        'Johnson',
        NULL,
        0,
        NULL,
        '<IndividualSurvey xmlns="http://schemas.microsoft.com/sqlserver/2004/07/adventure-works/IndividualSurvey"><TotalPurchaseYTD>0</TotalPurchaseYTD></IndividualSurvey>',
        '92C4279F-1207-48A3-8448-4636514EB7E3',
        '2009-01-08 00:00:00.000'
    FROM (
        SELECT 1 AS "dual"
    ) AS "dual"
    UNION ALL
    SELECT
        3,
        'EM',
        'Ms.',
        'Janis',
        'Lyn',
        'Joplin',
        NULL,
        0,
        NULL,
        '<IndividualSurvey xmlns="http://schemas.microsoft.com/sqlserver/2004/07/adventure-works/IndividualSurvey"><TotalPurchaseYTD>0</TotalPurchaseYTD></IndividualSurvey>',
        '92C4279F-1207-48A3-8448-4636514EB7E4',
        '2009-01-10 00:00:00.000'
    FROM (
        SELECT 1 AS "dual"
    ) AS "dual"
    UNION ALL
    SELECT
        4,
        'EM',
        'Mr.',
        'John',
        'Winston',
        'Lennon',
        NULL,
        0,
        NULL,
        '<IndividualSurvey xmlns="http://schemas.microsoft.com/sqlserver/2004/07/adventure-works/IndividualSurvey"><TotalPurchaseYTD>0</TotalPurchaseYTD></IndividualSurvey>',
        '92C4279F-1207-48A3-8448-4636514EB7E5',
        '2009-01-11 00:00:00.000'
    FROM (
        SELECT 1 AS "dual"
    ) AS "dual"
    UNION ALL
    SELECT
        5,
        'EM',
        'Ms.',
        'Billie',
        'Lady Day',
        'Holiday',
        NULL,
        0,
        NULL,
        '<IndividualSurvey xmlns="http://schemas.microsoft.com/sqlserver/2004/07/adventure-works/IndividualSurvey"><TotalPurchaseYTD>0</TotalPurchaseYTD></IndividualSurvey>',
        '92C4279F-1207-48A3-8448-4636514EB7E6',
        '2009-01-13 00:00:00.000'
    FROM (
        SELECT 1 AS "dual"
    ) AS "dual"
    UNION ALL
    SELECT
        6,
        'EM',
        'Mr.',
        'Borislav',
        'V',
        'Pekic',
        NULL,
        0,
        NULL,
        '<IndividualSurvey xmlns="http://schemas.microsoft.com/sqlserver/2004/07/adventure-works/IndividualSurvey"><TotalPurchaseYTD>0</TotalPurchaseYTD></IndividualSurvey>',
        '92C4279F-1207-48A3-8448-4636514EB7E7',
        '2009-01-14 00:00:00.000'
    FROM (
        SELECT 1 AS "dual"
    ) AS "dual"
    UNION ALL
    SELECT
        7,
        'EM',
        'Mr.',
        'Harold',
        'Stage',
        'Pinter',
        NULL,
        0,
        NULL,
        '<IndividualSurvey xmlns="http://schemas.microsoft.com/sqlserver/2004/07/adventure-works/IndividualSurvey"><TotalPurchaseYTD>0</TotalPurchaseYTD></IndividualSurvey>',
        '92C4279F-1207-48A3-8448-4636514EB7E8',
        '2009-01-15 00:00:00.000'
    FROM (
        SELECT 1 AS "dual"
    ) AS "dual"
    UNION ALL
    SELECT
        8,
        'EM',
        'Mr.',
        'Stojan',
        'Steve',
        'Teshic',
        NULL,
        0,
        NULL,
        '<IndividualSurvey xmlns="http://schemas.microsoft.com/sqlserver/2004/07/adventure-works/IndividualSurvey"><TotalPurchaseYTD>0</TotalPurchaseYTD></IndividualSurvey>',
        '92C4279F-1207-48A3-8448-4636514EB7E9',
        '2009-01-16 00:00:00.000'
    FROM (
        SELECT 1 AS "dual"
    ) AS "dual"
    UNION ALL
    SELECT
        9,
        'EM',
        'Ms.',
        'Mary',
        'Wollstonecraft',
        'Shelley',
        NULL,
        0,
        NULL,
        '<IndividualSurvey xmlns="http://schemas.microsoft.com/sqlserver/2004/07/adventure-works/IndividualSurvey"><TotalPurchaseYTD>0</TotalPurchaseYTD></IndividualSurvey>',
        '92C4279F-1207-48A3-8448-4636514EB7E1',
        '2009-01-17 00:00:00.000'
    FROM (
        SELECT 1 AS "dual"
    ) AS "dual"
    UNION ALL
    SELECT
        10,
        'EM',
        'Mr.',
        'William',
        'Poet',
        'Blake',
        NULL,
        0,
        NULL,
        '<IndividualSurvey xmlns="http://schemas.microsoft.com/sqlserver/2004/07/adventure-works/IndividualSurvey"><TotalPurchaseYTD>0</TotalPurchaseYTD></IndividualSurvey>',
        '92C4279F-1207-48A3-8448-4636514EB7D2',
        '2009-01-18 00:00:00.000'
    FROM (
        SELECT 1 AS "dual"
    ) AS "dual"
    ) "t" (
    "v0",
    "v1",
    "v2",
    "v3",
    "v4",
    "v5",
    "v6",
    "v7",
    "v8",
    "v9",
    "v10",
    "v11"
    );
    """,
               "SAP ASE":
               """
    CREATE TABLE TestTable (
        BusinessEntityID int NOT NULL,
        PersonType nchar(2) NOT NULL,
        Title nvarchar(8) NULL,
        FirstName nvarchar(50) NOT NULL,
        MiddleName nvarchar(50) NULL,
        LastName nvarchar(50) NOT NULL,
        Suffix nvarchar(10) NULL,
        EmailPromotion int NOT NULL,
        AdditionalContactInfo xml NULL,
        Demographics xml NULL,
        rowguid varchar NOT NULL,
        ModifiedDate datetime NOT NULL
    );

    INSERT INTO TestTable
    SELECT
    1,
    'EM',
    'Ms.',
    'Aretha',
    'Louise',
    'Franklin',
    NULL,
    0,
    NULL,
    '<IndividualSurvey xmlns="http://schemas.microsoft.com/sqlserver/2004/07/adventure-works/IndividualSurvey"><TotalPurchaseYTD>0</TotalPurchaseYTD></IndividualSurvey>',
    '92C4279F-1207-48A3-8448-4636514EB7E2',
    '2009-01-07 00:00:00.000'
    UNION ALL
    SELECT
    2,
    'EM',
    'Mr.',
    'Robert',
    'Leroy',
    'Johnson',
    NULL,
    0,
    NULL,
    '<IndividualSurvey xmlns="http://schemas.microsoft.com/sqlserver/2004/07/adventure-works/IndividualSurvey"><TotalPurchaseYTD>0</TotalPurchaseYTD></IndividualSurvey>',
    '92C4279F-1207-48A3-8448-4636514EB7E3',
    '2009-01-08 00:00:00.000'
    UNION ALL
    SELECT
    3,
    'EM',
    'Ms.',
    'Janis',
    'Lyn',
    'Joplin',
    NULL,
    0,
    NULL,
    '<IndividualSurvey xmlns="http://schemas.microsoft.com/sqlserver/2004/07/adventure-works/IndividualSurvey"><TotalPurchaseYTD>0</TotalPurchaseYTD></IndividualSurvey>',
    '92C4279F-1207-48A3-8448-4636514EB7E4',
    '2009-01-10 00:00:00.000'
    UNION ALL
    SELECT
    4,
    'EM',
    'Mr.',
    'John',
    'Winston',
    'Lennon',
    NULL,
    0,
    NULL,
    '<IndividualSurvey xmlns="http://schemas.microsoft.com/sqlserver/2004/07/adventure-works/IndividualSurvey"><TotalPurchaseYTD>0</TotalPurchaseYTD></IndividualSurvey>',
    '92C4279F-1207-48A3-8448-4636514EB7E5',
    '2009-01-11 00:00:00.000'
    UNION ALL
    SELECT
    5,
    'EM',
    'Ms.',
    'Billie',
    'Lady Day',
    'Holiday',
    NULL,
    0,
    NULL,
    '<IndividualSurvey xmlns="http://schemas.microsoft.com/sqlserver/2004/07/adventure-works/IndividualSurvey"><TotalPurchaseYTD>0</TotalPurchaseYTD></IndividualSurvey>',
    '92C4279F-1207-48A3-8448-4636514EB7E6',
    '2009-01-13 00:00:00.000'
    UNION ALL
    SELECT
    6,
    'EM',
    'Mr.',
    'Borislav',
    'V',
    'Pekic',
    NULL,
    0,
    NULL,
    '<IndividualSurvey xmlns="http://schemas.microsoft.com/sqlserver/2004/07/adventure-works/IndividualSurvey"><TotalPurchaseYTD>0</TotalPurchaseYTD></IndividualSurvey>',
    '92C4279F-1207-48A3-8448-4636514EB7E7',
    '2009-01-14 00:00:00.000'
    UNION ALL
    SELECT
    7,
    'EM',
    'Mr.',
    'Harold',
    'Stage',
    'Pinter',
    NULL,
    0,
    NULL,
    '<IndividualSurvey xmlns="http://schemas.microsoft.com/sqlserver/2004/07/adventure-works/IndividualSurvey"><TotalPurchaseYTD>0</TotalPurchaseYTD></IndividualSurvey>',
    '92C4279F-1207-48A3-8448-4636514EB7E8',
    '2009-01-15 00:00:00.000'
    UNION ALL
    SELECT
    8,
    'EM',
    'Mr.',
    'Stojan',
    'Steve',
    'Teshic',
    NULL,
    0,
    NULL,
    '<IndividualSurvey xmlns="http://schemas.microsoft.com/sqlserver/2004/07/adventure-works/IndividualSurvey"><TotalPurchaseYTD>0</TotalPurchaseYTD></IndividualSurvey>',
    '92C4279F-1207-48A3-8448-4636514EB7E9',
    '2009-01-16 00:00:00.000'
    UNION ALL
    SELECT
    9,
    'EM',
    'Ms.',
    'Mary',
    'Wollstonecraft',
    'Shelley',
    NULL,
    0,
    NULL,
    '<IndividualSurvey xmlns="http://schemas.microsoft.com/sqlserver/2004/07/adventure-works/IndividualSurvey"><TotalPurchaseYTD>0</TotalPurchaseYTD></IndividualSurvey>',
    '92C4279F-1207-48A3-8448-4636514EB7E1',
    '2009-01-17 00:00:00.000'
    UNION ALL
    SELECT
    10,
    'EM',
    'Mr.',
    'William',
    'Poet',
    'Blake',
    NULL,
    0,
    NULL,
    '<IndividualSurvey xmlns="http://schemas.microsoft.com/sqlserver/2004/07/adventure-works/IndividualSurvey"><TotalPurchaseYTD>0</TotalPurchaseYTD></IndividualSurvey>',
    '92C4279F-1207-48A3-8448-4636514EB7D2',
    '2009-01-18 00:00:00.000'
    ;
    """}


def script_output():
    script = 0
    while script != 3:
        print("""
    1. CREATE TABLE + INSERT INTO
    2. CREATE USER DEFINED TYPE
    """)
        script = int(
            input("Enter the number of the script which you would like to generate: "))
        dataSource = input("Which data source is the script for? ")

        if script == 1 and dataSource.casefold() == "sql server":
            print(createTable["SQL Server"])
        elif script == 1 and dataSource.casefold() == "oracle":
            print(createTable["Oracle"])
        elif script == 1 and dataSource.casefold() == "mysql":
            print(createTable["MySQL"])
        elif script == 1 and dataSource.casefold() == "teradata":
            print(createTable["Teradata"])
        elif script == 1 and dataSource.casefold() == "db2":
            print(createTable["DB2 LUW"])
        elif script == 1 and dataSource.casefold() == "sap ase":
            print(createTable["SAP ASE"])
        elif script == 1 and dataSource.casefold() == "postgresql":
            print(createTable["PostgreSQL"])
        elif script == 1 and dataSource.casefold() == "snowflake":
            print(createTable["Snowflake"])
        elif script == 1 and dataSource.casefold() == "mariadb":
            print(createTable["MariaDB"])
        elif script == 1 and dataSource.casefold() == "vertica":
            print(createTable["Vertica"])
        elif script == 1 and dataSource.casefold() == "ms access":
            print(createTable["MS Access"])
        elif script == 1 and dataSource.casefold() == "azure synapse":
            print(createTable["Azure Synapse"])
        else:
            print("Please choose a valid script or data source to generate.")


main()
