from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_get_developers():
    response = client.get('/developers')
    assert response.status_code == 200


def test_get_developer():
    response = client.get('/developers/665fc4adde4d1f2fc3556968')
    assert response.status_code == 200


def test_get_developer_skills():
    response = client.get('/developers/665fc4adde4d1f2fc3556968/skills')
    assert response.status_code == 200


def test_get_developer_experience():
    response = client.get('/developers/665fc4adde4d1f2fc3556968/experience')
    assert response.status_code == 200


def test_get_developer_languages():
    response = client.get('/developers/665fc4adde4d1f2fc3556968/languages')
    assert response.status_code == 200


def test_create_developer():
    response = client.post('/developers', json={

        "name": "Pablo paisa",
                "country": "Nica",
                "age": 26,
                "skills": [
                    {
                        "name": "Python",
                        "years": 5
                    },
                    {
                        "name": "JavaScript",
                        "years": 6
                    },
                    {
                        "name": "React",
                        "years": 2
                    }
                ],
        "experience": [
                    {
                        "title": "Software Developer",
                        "location": "Ecuador",
                        "start_date": "2021",
                        "end_date": "Present",
                        "organization": "Real Company"
                    }
                ],
        "languages": [
                    {
                        "name": "Spanish",
                        "level": "Native"
                    },
                    {
                        "name": "English",
                        "level": "Intermediate"
                    }
                ]
    }
    )
    assert response.status_code == 201



def test_update_developer():
    response = client.put('/developers/665fc4adde4d1f2fc3556968', json={

        "name": "Pablo nica",
                "country": "Nica",
                "age": 26,
                "skills": [
                    {
                        "name": "Python",
                        "years": 5
                    },
                    {
                        "name": "JavaScript",
                        "years": 6
                    },
                    {
                        "name": "React",
                        "years": 2
                    }
                ],
        "experience": [
                    {
                        "title": "Software Developer",
                        "location": "Ecuador",
                        "start_date": "2021",
                        "end_date": "Present",
                        "organization": "Real Company"
                    }
                ],
        "languages": [
                    {
                        "name": "Spanish",
                        "level": "Native"
                    },
                    {
                        "name": "English",
                        "level": "Intermediate"
                    }
                ]
    }
    )
    assert response.status_code == 201

def test_delete_developer():
    response = client.delete('/developers/665fc4adde4d1f2fc3556968')
    assert response.status_code == 201
    
def test_delete_developer_400():
    response = client.delete('/developers/665fc4adde4d1f2fc3556960')
    assert response.status_code == 400