-- @BLOCK
-- Clear
DROP TABLE Users;
DROP TABLE Items;

-- @BLOCK

CREATE TABLE Users(
    id VARCHAR(255) NOT NULL UNIQUE,
    email VARCHAR(255) NOT NULL UNIQUE,
    display_name VARCHAR NOT NULL UNIQUE(255),
    avatar TEXT,
    earth_coins INT
);

-- @BLOCK
CREATE TABLE Items(
    item_id INT PRIMARY KEY AUTO_INCREMENT,
    owner_id INT NOT NULL,
    item_name VARCHAR(255)
);


-- @BLOCK
INSERT INTO Users(id,email,display_name,avatar,earth_coins)
VALUES('id here','email here', 'display name here', 'None',0
);

-- @ BLOCK 
-- @BLOCK
INSERT INTO Items(owner_id,item_name)
VALUES ('owner id here', 'item name here')
);

-- @BLOCK
UPDATE Users
SET
earth_coins = 'newnumber'
WHERE id = 'user id';

-- @BLOCK
UPDATE Users
SET
avatar = 'avatar'
WHERE id = 'user id';
