from weather_agent import get_weather_data
def test_get_weather_success():
    api_key = "fb72866f2d6f4d878e35877b5ae44971"
    report = get_weather_data("London", api_key)
    assert "London" in report
    assert "temperature" in report
    assert "Error" not in report

def test_get_weather_failure():
    api_key = "fb72866f2d6f4d878e35877b5ae44971"
    report = get_weather_data("CityThatDoesNotExist", api_key)
    assert "Error" in report 

    
      
