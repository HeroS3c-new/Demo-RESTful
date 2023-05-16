from datetime import datetime
from flask import abort, make_response

#timestamp richiesta
def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

#struttura dati corsi
COURSES= {
    "Cybersecurity" : {
        "name_course" : "Cybersecurity",
        "number_of_credits" : 6,
        "timestamp" : get_timestamp(),
    }, 
    "Artificial_Intelligents" : {
        "name_course" :  "Artificial_Intelligents", 
        "number_credits" : 6,
        "timestamp" : get_timestamp(),
    },
    "Protocols" : {
        "name_course" : "Protocols",
        "number_of_credits" : 12,
        "timestamp" : get_timestamp(),
    },
}


def read_all():
    return list(COURSES.values())

def create(course): 
    name_course =  course.get("name_course")
    number_of_credits = course.get("number_of_credits","")

    if name_course not in COURSES:
        COURSES[name_course] = {
            "name_course": name_course,
            "number_of_credits": number_of_credits, 
            "timestamp" : get_timestamp(),
        }
        return COURSES[name_course], 201
    else : 
        abort(406, f"Course whit name{name_course} already exists",)

def read_one_course(name_course):
    if name_course in COURSES:
        return COURSES[name_course]
    else: 
        abort(406,f"Course whit name{name_course} not found",)
def update(name_course, course): 
    if name_course in COURSES: 
        COURSES[name_course]["number_of_credits"] = course.get("number_of_credits",COURSES[name_course]["number_of_credits"]) 
        COURSES[name_course]["timestamp"] = get_timestamp()
        return COURSES[name_course]
    else: 
        abort(404,f"Course whit name {name_course} not found",)
def delete(name_course): 
    if name_course in COURSES: 
        del COURSES[name_course]
        return make_response(f"{name_course} successfully deleted",200 )
    else: 
        abort(404, f"Course whit name {name_course} not found")
