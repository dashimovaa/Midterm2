

def calculateGPA(grades, credits):


  total_points = 0
  total_credits = 0
  for grade, credit in zip(grades, credits):
    grade_points = translateLetter(grade)
    total_points += grade_points * credit
    total_credits += credit
  return total_points / total_credits


def translateLetter(letter):

  translation_table = {
      'A+': 4.3,
      'A': 4.0,
      'A-': 3.7,
      'B+': 3.3,
      'B': 3.0,
      'B-': 2.7,
      'C+': 2.3,
      'C': 2.0,
      'C-': 1.7,
      'D+': 1.3,
      'D': 1.0,
      'D-': 0.7
  }

  return translation_table.get(letter, 0.0)


def translatePercentage(percentage):

  if percentage >= 95:
    return 'A+'
  elif percentage >= 90:
    return 'A'
  elif percentage >= 85:
    return 'A-'
  elif percentage >= 80:
    return 'B+'
  elif percentage >= 75:
    return 'B'
  elif percentage >= 70:
    return 'B-'
  elif percentage >= 65:
    return 'C+'
  elif percentage >= 60:
    return 'C'
  elif percentage >= 55:
    return 'C-'
  elif percentage >= 50:
    return 'D+'
  elif percentage >= 45:
    return 'D'
  elif percentage >= 40:
    return 'D-'
  else:
    return 'F'




grades = ['A+', 'B', 'C']
credits = [4, 3, 4]

gpa = calculateGPA(grades, credits)

print(f'GPA: {gpa}')


class Student:
    def __init__(self, name, num_courses, scores):
        self.name = name
        self.num_courses = num_courses
        self.scores = scores
        self._gpa = None
        self._status = None

    def calculateGPA(self):
        total_score = 0
        total_credits = 0

        for course, info in self.scores.items():
            total_score += info['score'] * info['credits']
            total_credits += info['credits']

        if total_credits == 0:
            return 0
        self._gpa = round(total_score / total_credits, 2)
        return self._gpa

    def setStatus(self):
        if self._gpa is None:
            self.calculateGPA()

        if self._gpa >= 1.0:
            self._status = 'Passed'
        else:
            self._status = 'Not Passed'

    def showGPA(self):
        if self._gpa is None:
            self.calculateGPA()
        print(f"{self.name}'s GPA is: {self._gpa}")

    def showStatus(self):
        if self._status is None:
            self.setStatus()  # Set status if not already set
        print(f"{self.name}'s status: {self._status}")



scores_data = {
    'math': {'score': 4.3, 'credits': 4},
    'chemistry': {'score': 3.3, 'credits': 3},
    'english': {'score': 4.0, 'credits': 4}
}


student1 = Student('Daniya', 3, scores_data)


student1.showGPA()
student1.showStatus()


def translateLetter(letters):

    letter_points = {
        'A+': 4.3, 'A': 4.0, 'A-': 3.7,
        'B+': 3.3, 'B': 3.0, 'B-': 2.7,
        'C+': 2.3, 'C': 2.0, 'C-': 1.7,
        'D+': 1.3, 'D': 1.0, 'D-': 0.7
    }
    return [letter_points.get(letter.strip(), 0) for letter in letters]


def calculateGPA(scores, credits):
    total_score = sum(scores)
    total_credits = sum(credits)
    return round(total_score / total_credits, 2) if total_credits > 0 else 0


with open("grades/credits.txt", 'r') as credits_file:
    credits = [int(line.strip()) for line in credits_file.readlines()]


students_gpas = []
courses = ["math", "chemistry", "english"]

for course in courses:
    with open(f"grades/{course}.txt", 'r') as grades_file:
        scores = translateLetter(grades_file.readlines())
        gpa = calculateGPA(scores, credits)
        students_gpas.append(gpa)


with open("grades/overallGPAs.txt", 'w') as overall_gpas_file:
    for gpa in students_gpas:
        overall_gpas_file.write(f"{gpa}\n")

#4 API. [10%]
#API stands for Application Programming Interface. It's a set of rules, protocols, and tools that allow different software applications to communicate with each other. APIs define the methods and data formats that applications can use to request and exchange information, enabling seamless interaction between various systems.
#Use cases of APIs are diverse and include:
#Integration: APIs facilitate the integration of different systems or services, allowing them to work together. For instance, integrating payment gateways into e-commerce websites.
#Data Access: They enable access to data or functionality of other services. Social media platforms often provide APIs for developers to access user data or post content programmatically.
#Building Applications: Developers use APIs to build new applications or enhance existing ones by leveraging functionalities offered by other services or platforms.
#APIs, while incredibly powerful in enabling seamless interaction between different software systems, do have limitations:
#Rate Limits: Many APIs have rate limits, which restrict the number of requests a user or application can make within a certain timeframe. Exceeding these limits can lead to temporary or permanent restrictions on access.
#Changes and Versioning: APIs can change over time. Updates or changes in API versions might lead to deprecated functionalities or alterations in the way data is structured or accessed. Developers relying on these APIs need to adapt their code accordingly.
#Security Concerns: If an API isn’t properly secured, it can pose security risks. Vulnerabilities such as insufficient authentication, data breaches, or unauthorized access might occur if security measures are not robust.
#Reliability and Downtime: Dependence on external APIs introduces the risk of downtime or interruptions. If the API provider experiences issues or undergoes maintenance, it can impact the functionality of applications relying on that API.
#Limited Functionality: Not all functionalities of a service may be exposed through its API. Some services might restrict certain features or data from being accessed or manipulated programmatically.
#Documentation and Support: Inadequate or unclear documentation can make it challenging for developers to understand and use an API effectively. Lack of robust support or community resources can also hinder the troubleshooting process.
import requests
api_key = 'YOUR_API_KEY'
base_url = 'http://api.openweathermap.org/data/2.5/weather'
city_name = 'London'
params = {
    'q': city_name,
    'appid': api_key,
    'units': 'metric'
}
response = requests.get(base_url, params=params)
if response.status_code == 200:
    data = response.json()
    city = data['name']
    weather = data['weather'][0]['description']
    temp = data['main']['temp']
    print(f'Weather in {city}: {weather}, Temperature: {temp}°C')
else:
    print('Failed to retrieve data')

#5 Socket. [10%]
#A socket is a software structure that allows programs to communicate over a network. It provides an endpoint for sending or receiving data between systems through the network. Sockets utilize specific protocols to establish connections, send data, and close connections.
#Use cases of sockets include:
#Network Communication: Sockets are fundamental for various network communication applications such as client-server architectures, where programs on different devices communicate with each other.
#Real-Time Data Transfer: They are used for real-time data transfer applications like chat applications, online gaming, and streaming services.
#Distributed Systems: Sockets enable communication between different components of distributed systems, allowing them to exchange information and work together.
import socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 12345
server_socket.bind((host, port))
server_socket.listen(5)
print('Server listening...')
while True:
    client_socket, addr = server_socket.accept()
    print(f'Got