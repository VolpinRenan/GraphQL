# flask_sqlalchemy/schema.py
import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from flask_sqlalchemy.models import Department, Employee
from sqlalchemy import *
from sqlalchemy.orm import (scoped_session, sessionmaker, relationship,
                            backref, session)
from sqlalchemy.ext.declarative import declarative_base

# engine = create_engine('sqlite:///database.sqlite3', convert_unicode=True)
# db = sessionmaker(autocommit=False, autoflush=False, bind=engine)

engine = create_engine('sqlite:///database.sqlite3', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
db = db_session()


class DepartmentObject(SQLAlchemyObjectType):
    class Meta:
        model = Department
        interfaces = (relay.Node, )


# class DepartmentConnection(relay.Connection):
#     class Meta:
#         node = Department


class EmployeeObject(SQLAlchemyObjectType):
    class Meta:
        model = Employee
        interfaces = (relay.Node, )


# class EmployeeConnection(relay.Connection):
#     class Meta:
#         node = Employee


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    # Allows sorting over multiple columns, by default over the primary key
    all_employees = SQLAlchemyConnectionField(EmployeeObject._meta.connection)#EmployeeConnection)
    # Disable sorting over this field
    all_departments = SQLAlchemyConnectionField(DepartmentObject._meta.connection, sort=None)#DepartmentConnection, sort=None)


# MUTATION CREATE
# create employ
class CreateDepartment(graphene.Mutation):
    class Arguments:
        # id = graphene.Int(required=False)
        name = graphene.String(required=True)
        hired_on = graphene.DateTime(required=True)
        # department_id = graphene.Int(required=True)
        department = graphene.String(required=True) # True

    depart = graphene.Field(lambda: DepartmentObject)
    employ = graphene.Field(lambda: EmployeeObject)

    ###, department_id, department):
    def mutate(self, info, name, hired_on, department):
        ###depart = Department(department=department, department_id=department_id)
        depart = Department(name=department)
        employ = Employee(name=name, hired_on=hired_on)

        if depart is not None:
            employ.department = depart

        # db.session.add(employ)
        # db.session.commit()
        db.add(employ)
        db.commit()

        return CreateDepartment(employ=employ)

class Mutation(graphene.ObjectType):
    create_deparment = CreateDepartment.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
