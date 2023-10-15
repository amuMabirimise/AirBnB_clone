#!/usr/bin/python3
"""The entry point of the command interpreter"""
import cmd
from datetime import datetime
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review

ClassDict = {
    "BaseModel": BaseModel,
    "User": User,
    "Place": Place,
    "State": State,
    "Amenity": Amenity,
    "City": City,
    "Review": Review,
}

class HBNBCommand(cmd.Cmd):
    """Command interpreter like in shell"""

    prompt = "(hbnb) "

    def emptyline(self):
        """it should not execute in an empty line"""
        pass

    def do_quit(self, line):
        """exiting command"""
        return True

    def do_EOF(self, line):
        """closing the programm"""
        return True

    def do_create(self, args):
        """this is where we create our instance"""
        if not args:
            print('** class name missing **')
            return
        class_name = args
        if class_name in ClassDict:
            newInstance = ClassDict[class_name]()
            newInstance.save()
            print(newInstance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, args):
        """our json string being printed"""
        if not args:
            print('** class name missing **')
            return
        
        newInstance = args.split()
        class_name = newInstance[0]
        if class_name not in ClassDict:
            print("** class doesn't exist **")
            return
        if len(newInstance) < 2:
            print('** instance id missing **')
            return
        
        class_id = newInstance[1]
        storage_list = storage.all()
        for i in storage_list:
            if (class_id == storage_list[i].to_dict()["id"]):
                print(str(storage_list[i]))
            else:
                print("** no instance found **")

    def do_destroy(self, args):
        """where we destroy storage"""
        if not args:
            print('** class name missing **')
            return
        new_args = args.split()
        class_name = new_args[0]
        if class_name not in ClassDict:
            print("** class doesn't exist **")
            return
        if len(new_args) < 2:
            print("** instance id missing **")
            return
        class_id = new_args[1]
        storage_list = storage.all()
        for i, val in storage_list.items():
            if (class_id == val.id):
                del storage_list[i] 
                storage.save()
                break
                return
            else:
                print("** no instance found **")

    def do_all(self, args=None):
        """printing available strings"""
        if len(args) == 1 and args not in ClassDict:
            print("** class doesn't exist **")
            return
        new_list = []
        storage_list = storage.all()
        for instance in storage_list:
            if (args == storage_list[instance].to_dict()["__class__"]):
                new_list.append(str(storage_list[instance]))
                print(new_list)

    def do_update(self, args):
        """saving and changing the attribute instance"""
        new_args = args.split()
        if not new_args:
            print("** class name missing **")
            return
        class_name = new_args[0]
        if class_name not in ClassDict:
            print("** class doesn't exist **")
            return
        if len(new_args) < 2:
            print("** instance id missing **")
            return
        obj_id = new_args[1]
        storage_list = storage.all()
        for i in storage_list:
            if (obj_id == storage_list[i].to_dict()["id"]):
                if len(new_args) < 3:
                    print("** attribute name missing **")
                    return
                else:
                        attribute_name = new_args[2]
                        if len(new_args) < 4:
                            print("** value missing **")
                            return
                        else:
                            attribute_value = new_args[3]
                            #instance = storage.all()["{}.{}".format(class_name, obj_id)]
                            setattr(storage_list[i], attribute_name, attribute_value)
                            storage_list[i].save()
            else:
                print("** no instance found **")
                return
        
              
if __name__ == '__main__':
    HBNBCommand().cmdloop()
