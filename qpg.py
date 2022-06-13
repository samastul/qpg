import sqlite3
import random

sql = sqlite3.connect("Questionpaper.db")
cur = sql.cursor()


def questionEntry(subj, ques, marks, diff, topic):
    new = 'create table if not exists ' + subj + ' (ques VARCHAR, marks INT(2), diff INT(1),)'
    cur.execute(new)
    insert = "INSERT INTO " + subj + """
                          (ques, marks, diff, topic) 
                          VALUES (?, ?, ?, ?);"""

    data = (ques, marks, diff, topic)
    cur.execute(insert, data)
    sql.commit()


def viewQuestions(subj):
    cur.execute("SELECT ques,marks FROM " + subj)
    questions = cur.fetchall()

    for i in questions:
        print(questions.index(i) + 1, end='')
        print(" ", i)


def questionSelector(subj, pattern, topic):
    # topic = [0]
    if pattern == "MST":

        topic_tuple = tuple(topic)
        cur.execute("SELECT ques FROM " + subj + " WHERE marks=? AND topic IN{};".format(topic_tuple), (2,))
        questions2 = [x[0] for x in cur.fetchall()]
        cur.execute("SELECT ques FROM " + subj + " WHERE marks=? AND topic IN{};".format(topic_tuple), (4,))
        questions4 = [x[0] for x in cur.fetchall()]
        cur.execute("SELECT ques FROM " + subj + " WHERE marks=? AND topic IN{};".format(topic_tuple), (8,))
        questions12 = [x[0] for x in cur.fetchall()]

        paper = random.sample(questions2, k=2) + random.sample(questions4, k=3) + random.sample(questions12, k=1)

        for i in paper:
            print('Q', end="")
            print(paper.index(i) + 1, end=':')
            print(" ", i)

    elif pattern == "ESE":
        topic_tuple = tuple(topic)
        cur.execute("SELECT ques FROM " + subj + " WHERE marks=? AND topic IN{};".format(topic_tuple), (2,))
        questions2 = [x[0] for x in cur.fetchall()]
        cur.execute("SELECT ques FROM " + subj + " WHERE marks=? AND topic IN{};".format(topic_tuple), (4,))
        questions4 = [x[0] for x in cur.fetchall()]
        cur.execute("SELECT ques FROM " + subj + " WHERE marks=? AND topic IN{};".format(topic_tuple), (8,))
        questions12 = [x[0] for x in cur.fetchall()]

        paper = random.sample(questions2, k=8) + random.sample(questions4, k=5) + random.sample(questions12, k=2)

        for i in paper:
            print('Q', end="")
            print(paper.index(i) + 1, end=':')
            print(" ", i)
    else:
        print("unrecognisable paper pattern!")


# questionEntry("CD", "Write is the difference between pass and parser?", 2, 2, 2)
# viewQuestions("CD")

sub = input("enter subject: ")
patt = input("enter pattern: ")
chap = []

n = int(input("Enter number of chapters : "))

print("chapter numbers: ")
for i in range(0, n):
    ele = int(input())

    chap.append(ele)
print(chap)

questionSelector(sub, patt, chap)
