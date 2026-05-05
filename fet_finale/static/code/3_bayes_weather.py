p_sunny = 0.3
p_cloudy = 0.5
p_rainy = 0.2

p_sunny_sunny = 0.6
p_cloudy_cloudy = 0.5
p_rainy_rainy = 0.5

p_sunny_cloudy = 0.3
p_sunny_rainy = 0.1

p_cloudy_sunny = 0.3
p_cloudy_rainy = 0.4

p_rainy_sunny = 0.1
p_rainy_cloudy = 0.3


def cal_prob_weather():
    p_today = p_rainy
    return p_today * p_sunny_rainy * p_cloudy_sunny * p_rainy_cloudy


if __name__ == "__main__":
    print(cal_prob_weather())




#simpler

# # given prob.
# P_rain = 0.3            # P(A)
# P_no_rain = 0.7         # P(~A)
# P_forecast_rain_rain = 0.8   # P(B|A)
# P_forecast_rain_sunny = 0.1  # P(B|~A)

# # Bayes theorem
# P_rain_given_forecast = (P_forecast_rain_rain * P_rain) / \
#                         ((P_forecast_rain_rain * P_rain) + (P_forecast_rain_sunny * P_no_rain))

# print(f"Probability it is actually raining given forecast says rain: {P_rain_given_forecast:.2f}")