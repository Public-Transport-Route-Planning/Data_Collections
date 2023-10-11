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
                    "05:30:00", format="%H:%M:%S"
                ) and current_time < pd.to_datetime("06:30:00", format="%H:%M:%S"):
                    service_interval = 9
                elif current_time >= pd.to_datetime(
                    "06:30:00", format="%H:%M:%S"
                ) and current_time < pd.to_datetime("08:30:00", format="%H:%M:%S"):
                    service_interval = 6
                elif current_time >= pd.to_datetime(
                    "08:30:00", format="%H:%M:%S"
                ) and current_time < pd.to_datetime("16:30:00", format="%H:%M:%S"):
                    service_interval = 9
                elif current_time >= pd.to_datetime(
                    "16:30:00", format="%H:%M:%S"
                ) and current_time < pd.to_datetime("19:30:00", format="%H:%M:%S"):
                    service_interval = 6
                else:
                    service_interval = 9

                current_time = initial_time + pd.Timedelta(minutes=service_interval)

                train_num += 1

            initial_time = current_time

    return pd.DataFrame(time_travel)


travel_times = [
    4,
    3,
    2,
    2,
    2,
    2,
    3,
    3,
    1,
    2,
    4,
    2,
    3,
    2,
    2,
]  # add travel times for all stations

station_route = "../../../station_route/data/mrt/mrt_p_route.csv"
station_route = pd.read_csv(station_route)

stations = station_route[station_route["direction"] == "go"][
    ["direction", "sid", "sname"]
].values.tolist()
start_time = "05:30:00"  #
end_time = "22:47:00"
num_journeys = 3


time_travel = generate_time_travel(
    stations, start_time, end_time, num_journeys, travel_times
)

train_num = time_travel["train_num"].max()

# add the last train starting at 00:00 AM ##
train_time1 = pd.to_datetime("22:47:00", format="%H:%M:%S")
train_data1 = []

for i in range(len(stations) - 1):
    station1 = stations[i][2]
    station2 = stations[i + 1][2]
    travel_time = travel_times[i]

    train_data1.append(
        {
            "train_num": train_num + 1,
            "direction": stations[i][0],
            "sid1": stations[i][1],
            "sname1": station1,
            "sid2": stations[i + 1][1],
            "sname2": station2,
            "ts1": train_time1.strftime("%H:%M:%S"),
            "ts2": (train_time1 + pd.Timedelta(minutes=travel_time)).strftime(
                "%H:%M:%S"
            ),
        }
    )
    train_time1 += pd.Timedelta(minutes=travel_time)

time_travel = pd.concat(
    [time_travel.iloc[:1980], pd.DataFrame(train_data1)], ignore_index=True
)


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
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
]

time_travel_per_day = []

# Loop through each day of the week
for day in days_of_week:
    day_df = time_travel.copy()

    day_df["day_of_week"] = day

    if day == "Monday":
        day_df.loc[(day_df["ts1"] >= "00:00:00") & (day_df["ts1"] < "03:00:00"), "day_of_week"] = "Tuesday"
    elif day == "Tuesday":
        day_df.loc[(day_df["ts1"] >= "00:00:00") & (day_df["ts1"] < "03:00:00"), "day_of_week"] = "Wednesday"
    elif day == "Wednesday":
        day_df.loc[(day_df["ts1"] >= "00:00:00") & (day_df["ts1"] < "03:00:00"), "day_of_week"] = "Thursday"
    elif day == "Thursday":
        day_df.loc[(day_df["ts1"] >= "00:00:00") & (day_df["ts1"] < "03:00:00"), "day_of_week"] = "Friday"
    elif day == "Friday":
        day_df.loc[(day_df["ts1"] >= "00:00:00") & (day_df["ts1"] < "03:00:00"), "day_of_week"] = "Saturday"


    time_travel_per_day.append(day_df)


time_travel = pd.concat(time_travel_per_day, ignore_index=True)
time_travel["route_id"] = "MRT-P"
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


route_weekend = pd.read_csv("p_w_go.csv")

time_travel = pd.concat([time_travel, route_weekend], axis=0)
time_travel.to_csv("p_go.csv", index=False)


##################################################################################


# import pandas as pd


# def generate_time_travel(stations, start_time, end_time, num_journeys, travel_times):
#     time_travel = []

#     for journey in range(num_journeys):
#         current_time = pd.to_datetime(start_time, format="%H:%M:%S")
#         end_datetime = pd.to_datetime(end_time, format="%H:%M:%S")

#         train_num = 1
#         initial_time = current_time

#         while current_time <= end_datetime:
#             for i in range(len(stations) - 1):
#                 station1 = stations[i][2]
#                 station2 = stations[i + 1][2]
#                 travel_time = travel_times[i]

#                 time_travel.append(
#                     {
#                         "train_num": train_num,
#                         "direction": stations[i][0],
#                         "sid1": stations[i][1],
#                         "sname1": station1,
#                         "sid2": stations[i + 1][1],
#                         "sname2": station2,
#                         "ts1": current_time.strftime("%H:%M:%S"),
#                         "ts2": (
#                             current_time + pd.Timedelta(minutes=travel_time)
#                         ).strftime("%H:%M:%S"),
#                     }
#                 )
#                 current_time += pd.Timedelta(minutes=travel_time)

#             if journey < num_journeys - 1:
#                 if current_time >= pd.to_datetime(
#                     "05:30:00", format="%H:%M:%S"
#                 ) and current_time < pd.to_datetime("06:30:00", format="%H:%M:%S"):
#                     service_interval = 9
#                 elif current_time >= pd.to_datetime(
#                     "06:30:00", format="%H:%M:%S"
#                 ) and current_time < pd.to_datetime("08:30:00", format="%H:%M:%S"):
#                     service_interval = 6
#                 elif current_time >= pd.to_datetime(
#                     "08:30:00", format="%H:%M:%S"
#                 ) and current_time < pd.to_datetime("16:30:00", format="%H:%M:%S"):
#                     service_interval = 9
#                 elif current_time >= pd.to_datetime(
#                     "16:30:00", format="%H:%M:%S"
#                 ) and current_time < pd.to_datetime("19:30:00", format="%H:%M:%S"):
#                     service_interval = 6
#                 else:
#                     service_interval = 9

#                 current_time = initial_time + pd.Timedelta(minutes=service_interval)

#                 train_num += 1

#             initial_time = current_time

#     return pd.DataFrame(time_travel)


# travel_times = [
#     6,
#     2,
#     3,
#     3,
#     3,
#     2,
#     2,
#     2,
#     3,
#     2,
#     2,
#     2,
#     2,
#     3,
#     3,
# ]  # add travel times for all stations

# station_route = "../../../station_route/data/mrt/mrt_p_route.csv"
# station_route = pd.read_csv(station_route)

# stations = station_route[station_route["direction"] == "back"][
#     ["direction", "sid", "sname"]
# ].values.tolist()
# start_time = "06:00:00"  #
# end_time = "23:24:00"
# num_journeys = 3


# time_travel = generate_time_travel(
#     stations, start_time, end_time, num_journeys, travel_times
# )

# train_num = time_travel["train_num"].max()

# # add the last train starting at 00:00 AM ##
# train_time1 = pd.to_datetime("23:24:00", format="%H:%M:%S")
# train_data1 = []

# for i in range(len(stations) - 1):
#     station1 = stations[i][2]
#     station2 = stations[i + 1][2]
#     travel_time = travel_times[i]

#     train_data1.append(
#         {
#             "train_num": train_num + 1,
#             "direction": stations[i][0],
#             "sid1": stations[i][1],
#             "sname1": station1,
#             "sid2": stations[i + 1][1],
#             "sname2": station2,
#             "ts1": train_time1.strftime("%H:%M:%S"),
#             "ts2": (train_time1 + pd.Timedelta(minutes=travel_time)).strftime(
#                 "%H:%M:%S"
#             ),
#         }
#     )
#     train_time1 += pd.Timedelta(minutes=travel_time)


# time_travel = pd.concat(
#     [time_travel.iloc[:1995], pd.DataFrame(train_data1)], ignore_index=True
# )


# time_travel["hrs"] = time_travel["ts1"].str.split(":").str[0].astype(int)

# for i in range(len(stations) - 1):
#     station1 = stations[i][2]
#     station2 = stations[i + 1][2]
#     travel_time = travel_times[i]

#     time_travel.loc[time_travel["sid1"] == station1, "sid1"] = stations[i][1]
#     time_travel.loc[time_travel["sid2"] == station2, "sid2"] = stations[i + 1][1]

# time_travel["ts1"] = pd.to_datetime(time_travel["ts1"], format="%H:%M:%S")
# time_travel["ts2"] = pd.to_datetime(time_travel["ts2"], format="%H:%M:%S")

# time_travel["mins"] = time_travel.apply(
#     lambda row: ((row["ts2"] - row["ts1"]).seconds / 60)
#     if row["ts2"] >= row["ts1"]
#     else (
#         (
#             (pd.to_datetime("23:59:59", format="%H:%M:%S") - row["ts1"]).seconds
#             + (row["ts2"] - pd.to_datetime("00:00:00", format="%H:%M:%S")).seconds
#         )
#         / 60
#     ),
#     axis=1,
# )


# time_travel["ts1"] = time_travel["ts1"].dt.strftime("%H:%M:%S")
# time_travel["ts2"] = time_travel["ts2"].dt.strftime("%H:%M:%S")
# days_of_week = [
#     "Monday",
#     "Tuesday",
#     "Wednesday",
#     "Thursday",
#     "Friday",
# ]

# time_travel_per_day = []

# # Loop through each day of the week
# for day in days_of_week:
#     day_df = time_travel.copy()

#     day_df["day_of_week"] = day

#     if day == "Monday":
#         day_df.loc[(day_df["ts1"] >= "00:00:00") & (day_df["ts1"] < "03:00:00"), "day_of_week"] = "Tuesday"
#     elif day == "Tuesday":
#         day_df.loc[(day_df["ts1"] >= "00:00:00") & (day_df["ts1"] < "03:00:00"), "day_of_week"] = "Wednesday"
#     elif day == "Wednesday":
#         day_df.loc[(day_df["ts1"] >= "00:00:00") & (day_df["ts1"] < "03:00:00"), "day_of_week"] = "Thursday"
#     elif day == "Thursday":
#         day_df.loc[(day_df["ts1"] >= "00:00:00") & (day_df["ts1"] < "03:00:00"), "day_of_week"] = "Friday"
#     elif day == "Friday":
#         day_df.loc[(day_df["ts1"] >= "00:00:00") & (day_df["ts1"] < "03:00:00"), "day_of_week"] = "Saturday"


#     time_travel_per_day.append(day_df)


# time_travel = pd.concat(time_travel_per_day, ignore_index=True)
# time_travel["route_id"] = "MRT-P"
# time_travel = time_travel[
#     [
#         "train_num",
#         "route_id",
#         "direction",
#         "sid1",
#         "sname1",
#         "sid2",
#         "sname2",
#         "ts1",
#         "ts2",
#         "mins",
#         "hrs",
#         "day_of_week",
#     ]
# ]


# route_weekend = pd.read_csv("p_w_back.csv")
# time_travel = pd.concat([time_travel, route_weekend], axis=0)
# time_travel.to_csv("p_back.csv", index=False)
