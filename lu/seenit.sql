drop database if exists seenitdb;
create database seenitdb;
use seenitdb;

CREATE TABLE IF NOT EXISTS user (
  u_id INT NOT NULL,
  pwd VARCHAR(45) NULL,
  u_name VARCHAR(45) NULL,
  email VARCHAR(45) NULL,
  PRIMARY KEY (u_id)
);

CREATE TABLE IF NOT EXISTS seenit (
  s_id INT NOT NULL,
  category VARCHAR(45) NULL,
  creater_id INT NOT NULL,
  PRIMARY KEY (s_id),
  FOREIGN KEY (creater_id)
  REFERENCES user(u_id)
  ON DELETE CASCADE
  ON UPDATE CASCADE);

CREATE TABLE IF NOT EXISTS post (
  p_id INT NOT NULL,
  p_content VARCHAR(255) NULL,
  seenit_id INT NOT NULL,
  author_id INT NOT NULL,
  PRIMARY KEY (p_id),
  FOREIGN KEY (seenit_id)
  REFERENCES seenit (s_id)
  ON DELETE CASCADE
  ON UPDATE CASCADE,
  FOREIGN KEY (author_id)
  REFERENCES user (u_id)
  ON DELETE CASCADE
  ON UPDATE CASCADE);

CREATE TABLE IF NOT EXISTS comment (
  c_id INT NOT NULL,
  c_content VARCHAR(255) NULL,
  author_id INT NOT NULL,
  post_id INT NOT NULL,
  PRIMARY KEY (c_id),
  FOREIGN KEY (author_id)
  REFERENCES user (u_id)
  ON DELETE CASCADE
  ON UPDATE CASCADE,
  FOREIGN KEY (post_id)
  REFERENCES post (p_id)
  ON DELETE CASCADE
  ON UPDATE CASCADE);

CREATE TABLE IF NOT EXISTS post_upvote (
  pu_id INT NOT NULL,
  author_id INT NOT NULL,
  post_id INT NOT NULL,
  PRIMARY KEY (pu_id),
  FOREIGN KEY (author_id)
  REFERENCES user (u_id)
  ON DELETE CASCADE
  ON UPDATE CASCADE,
  FOREIGN KEY (post_id)
  REFERENCES post (p_id)
  ON DELETE CASCADE
  ON UPDATE CASCADE);

CREATE TABLE IF NOT EXISTS post_downvote (
  pd_id INT NOT NULL,
  author_id INT NOT NULL,
  post_id INT NOT NULL,
  PRIMARY KEY (pd_id),
  FOREIGN KEY (author_id)
  REFERENCES user (u_id)
  ON DELETE CASCADE
  ON UPDATE CASCADE,
  FOREIGN KEY (post_id)
  REFERENCES post (p_id)
  ON DELETE CASCADE
  ON UPDATE CASCADE);

CREATE TABLE IF NOT EXISTS comment_downvote (
  cd_id INT NOT NULL,
  author_id INT NOT NULL,
  comment_id INT NOT NULL,
  PRIMARY KEY (cd_id),
  FOREIGN KEY (author_id)
  REFERENCES user (u_id)
  ON DELETE CASCADE
  ON UPDATE CASCADE,
  FOREIGN KEY (comment_id)
  REFERENCES comment (c_id)
  ON DELETE CASCADE
  ON UPDATE CASCADE);

CREATE TABLE IF NOT EXISTS comment_upvote (
  cu_id INT NOT NULL,
  author_id INT NOT NULL,
  comment_id INT NOT NULL,
  PRIMARY KEY (cu_id),
  FOREIGN KEY (author_id)
  REFERENCES user (u_id)
  ON DELETE CASCADE
  ON UPDATE CASCADE,
  FOREIGN KEY (comment_id)
  REFERENCES comment (c_id)
  ON DELETE CASCADE
  ON UPDATE CASCADE);

INSERT user VALUES
(1,'Andy','andy@gmail.com'),
(2,'Bob','bob@sjsu.edu'),
(3,'Chris','chris@yahoo.com'),
(4,'Evan','evan@gmail.com');

INSERT seenit VALUES
(1,'news',2),
(2,'gaming',4),
(3,'funny',1),
(4,'pics',3);

INSERT post (p_id,p_content,seenit_id,author_id) VALUES
(1,'Beautiful sunset reflecting on the sea.',4,2),
(2,'Animal shelters across U.S. teach cats how to high five to make them more attractive for adoption',1,3),
(3,'This is how my fathers dog says hello to me when I go to see him',3,4),
(4,'Is this the game that everyone is talking about [OC]',2,1);

INSERT comment(c_id,c_content,author_id,post_id) VALUES
(1,'cool',2,1),
(2,'LOL',3,3),
(3,'beautiful',4,1),
(4,'funny',3,2);

INSERT post_upvote(pu_id,author_id,post_id) VALUES
(1,1,1),
(2,2,2),
(3,3,3),
(4,4,4),
(5,1,2),
(6,1,3),
(7,1,4); 