import pandas as pd


def generate_time_travel(stations, start_time, end_time, num_journeys, travel_times):
    time_travel = []

    for journey in range(num_journeys):
        current_time = pd.to_datetime(start_time, format="%H:%M:%S")
        end_datetime = pd.to_datetime(end_time, format="%H:%M:%S")

        train_num = 1
        initial_time = current_time

        while current_time <= end_datetime:
            for i in range(len(stations) - 1):
                station1 = stations[i][2]
                station2 = stations[i + 1][2]
                travel_time = travel_times[i]

                time_travel.append(
                    {
                        "train_num": train_num,
                        "direction": stations[i][0],
                        "sid1": stations[i][1],
                        "sname1": station1,
                        "sid2": stations[i + 1][1],
                        "sname2": station2,
                        "ts1": current_time.strftime("%H:%M:%S"),
                        "ts2": (
                            current_time + pd.Timedelta(minutes=travel_time)
                        ).strftime("%H:%M:%S"),
                    }
                )
                current_time += pd.Timedelta(minutes=travel_time)

            if journey < num_journeys - 1:
                if current_time >= pd.to_datetime(
                    "06:00:00", format="%H:%M:%S"
                ) and current_time < pd.to_datetime("20:00:00", format="%H:%M:%S"):
                    service_interval = 10
                elif current_time >= pd.to_datetime(
                    "20:00:00", format="%H:%M:%S"
                ) and current_time < pd.to_datetime("21:00:00", format="%H:%M:%S"):
                    service_interval = 10
                else:
                    service_interval = 10

                current_time = initial_time + pd.Timedelta(minutes=service_interval)

                train_num += 1

            initial_time = current_time

    return pd.DataFrame(time_travel)


# travel_times = [
#     2,  # pk01 -> pk02
#     2,
#     2,
#     2,
#     2,
#     2,
#     2,
#     2,
#     2,
#     2,
#     1,
#     2,
#     2,
#     1,
#     2,
#     2,
#     1,
#     2,
#     2,
#     1,
#     2,
#     2,
#     2,
#     2,
#     2,
#     2,
#     2,
#     2,
#     2,
#     2,
# ]

travel_times = [
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    1,
    2,
    2,
    1,
    2,
    2,
    2,
    2,
    1,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,  # pk02 ->pk01
]

station_route = "../../../data_station_route/data/mrt/mrt_pi_route.csv"
station_route = pd.read_csv(station_route)
stations = station_route[station_route["direction"] == "back"][
    ["direction", "sid", "sname"]
].values.tolist()
start_time = "06:00:00"  #
end_time = "22:00:00"
num_journeys = 3


time_travel = generate_time_travel(
    stations, start_time, end_time, num_journeys, travel_times
)

train_num = time_travel["train_num"].max()


time_travel = pd.concat([time_travel.iloc[:2813]], ignore_index=True)


time_travel["hrs"] = time_travel["ts1"].str.split(":").str[0].astype(int)

for i in range(len(stations) - 1):
    station1 = stations[i][2]
    station2 = stations[i + 1][2]
    travel_time = travel_times[i]

    time_travel.loc[time_travel["sid1"] == station1, "sid1"] = stations[i][1]
    time_travel.loc[time_travel["sid2"] == station2, "sid2"] = stations[i + 1][1]

time_travel["ts1"] = pd.to_datetime(time_travel["ts1"], format="%H:%M:%S")
time_travel["ts2"] = pd.to_datetime(time_travel["ts2"], format="%H:%M:%S")

time_travel["mins"] = time_travel.apply(
    lambda row: ((row["ts2"] - row["ts1"]).seconds / 60)
    if row["ts2"] >= row["ts1"]
    else (
        (
            (pd.to_datetime("23:59:59", format="%H:%M:%S") - row["ts1"]).seconds
            + (row["ts2"] - pd.to_datetime("00:00:00", format="%H:%M:%S")).seconds
        )
        / 60
    ),
    axis=1,
)


time_travel["ts1"] = time_travel["ts1"].dt.strftime("%H:%M:%S")
time_travel["ts2"] = time_travel["ts2"].dt.strftime("%H:%M:%S")
days_of_week = [
    "Saturday",
    "Sunday",
]

time_travel_per_day = []

# Loop through each day of the week
for day in days_of_week:
    day_df = time_travel.copy()

    day_df["day_of_week"] = day

    if day == "Saturday":
        day_df.loc[
            (day_df["ts1"] >= "00:00:00") & (day_df["ts1"] < "03:00:00"), "day_of_week"
        ] = "Sunday"
    elif day == "Sunday":
        day_df.loc[
            (day_df["ts1"] >= "00:00:00") & (day_df["ts1"] < "03:00:00"), "day_of_week"
        ] = "Monday"

    time_travel_per_day.append(day_df)


time_travel = pd.concat(time_travel_per_day, ignore_index=True)
time_travel["route_id"] = "MRT-PI"
time_travel = time_travel[
    [
        "train_num",
        "route_id",
        "direction",
        "sid1",
        "sname1",
        "sid2",
        "sname2",
        "ts1",
        "ts2",
        "mins",
        "hrs",
        "day_of_week",
    ]
]
time_travel.to_csv("pi_w_back.csv", index=False)
