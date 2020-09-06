from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime, timedelta
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///todo.db?check_same_thread=False')
Base = declarative_base()

class Table(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String)
    deadline = Column(Date, default=datetime.today())

    def __repr__(self):
        return self.task

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


while True:
    print()
    print("""1) Today's tasks
2) Week's tasks
3) All tasks
4) Missed tasks
5) Add task
6) Delete task
0) Exit""")
    n = int(input())
    print()

    if n == 1:
        today = datetime.today()
        print("Today", today.day, today.strftime('%b'))
        sp = session.query(Table).filter(Table.deadline == today.date()).all()
        if len(sp) == 0:
            print("Nothing to do!")
        else:
            print(sp)

    elif n == 2:
        week = {0: 'Monday', 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday",
                5: "Saturday", 6: "Sunday", 7: 'Monday', 8: "Tuesday", 9: "Wednesday",
                10: "Thursday", 11: "Friday", 12: "Saturday"}
        today = datetime.today()
        n = today.weekday()
        for i in range(n, n+7):
            print(week[i], today.day, today.strftime('%b'))
            sp = session.query(Table).filter(Table.deadline == today.date()).all()
            today += timedelta(days=1)
            if len(sp) == 0:
                print("Nothing to do!")
            else:
                a = 1
                for t in sp:
                    print(str(a) + '.', sp[a - 1])
                    a += 1
            print()

    elif n == 3:
        print("All tasks:")
        sp = session.query(Table.task, Table.deadline).order_by(Table.deadline).all()
        if len(sp) == 0:
            print("Nothing to do!")
        else:
            a = 1
            for t in sp:
                print(str(a) + '.', t[0] + '.', t[1].day, t[1].strftime('%b'))
                a += 1

    elif n == 4:
        print("Missed tasks:")
        today = datetime.today()
        sp = session.query(Table.task, Table.deadline).filter(Table.deadline < today.date()).order_by(Table.deadline).all()
        if len(sp) == 0:
            print("Nothing to do!")
        else:
            a = 1
            for t in sp:
                print(str(a) + '.', t[0] + '.', t[1].day, t[1].strftime('%b'))
                a += 1

    elif n == 5:
        print("Enter task")
        t = input()
        print("Enter deadline")
        dead = input().split("-")
        d = datetime(int(dead[0]), int(dead[1]), int(dead[2]))
        new_row = Table(task=t, deadline=d)
        session.add(new_row)
        session.commit()
        print("The task has been added!")
        print()

    elif n == 6:
        print("Choose the number of the task you want to delete:")
        sp = session.query(Table.task, Table.deadline).order_by(Table.deadline).all()
        if len(sp) == 0:
            print("Nothing to do!")
        else:
            dt = {}
            a = 1
            for t in sp:
                print(str(a) + '.', t[0] + '.', t[1].day, t[1].strftime('%b'))
                dt[a] = [t[0], t[1]]
                a += 1
        t = int(input())
        spec = session.query(Table).filter(Table.deadline == dt[t][1], Table.task == dt[t][0]).all()
        session.delete(spec[0])
        session.commit()
        print("The task has been deleted!")
        print()

    else:
        print("Bye!")
        break
