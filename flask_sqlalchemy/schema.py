# flask_sqlalchemy/schema.py
import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from flask_sqlalchemy.models import Department, Employee


class Department(SQLAlchemyObjectType):
    class Meta:
        model = Department
        interfaces = (relay.Node, )


# class DepartmentConnection(relay.Connection):
#     class Meta:
#         node = Department


class Employee(SQLAlchemyObjectType):
    class Meta:
        model = Employee
        interfaces = (relay.Node, )


# class EmployeeConnection(relay.Connection):
#     class Meta:
#         node = Employee


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    # Allows sorting over multiple columns, by default over the primary key
    all_employees = SQLAlchemyConnectionField(Employee._meta.connection)#EmployeeConnection)
    # Disable sorting over this field
    all_departments = SQLAlchemyConnectionField(Department._meta.connection, sort=None)#DepartmentConnection, sort=None)

schema = graphene.Schema(query=Query)
