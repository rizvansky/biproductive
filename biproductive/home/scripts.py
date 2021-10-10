import numpy as np
import pandas as pd

from habits.scripts import load_last_n_days_habit_usage
from productivity.scripts import load_last_n_days_productivity_checks


def discretize_correlation(coefficient: np.float64):
    if coefficient > 0.8:
        return "Positive"
    elif coefficient < -0.8:
        return "Negative"
    elif np.isnan(coefficient):
        return "Lacks data"
    else:
        return "No correlation found"


def correlation(user):
    habit_usage = load_last_n_days_habit_usage(user, 7)
    habit_usage = pd.DataFrame(habit_usage)
    productivity = load_last_n_days_productivity_checks(user, 7)
    productivity = pd.DataFrame(productivity)
    binary_habit_usage: pd.DataFrame = habit_usage.replace(['+', '-', ' '], [1, 0, np.NaN])
    correlation_df = binary_habit_usage.corrwith(productivity['brain-activity'])
    correlation_df = pd.DataFrame(correlation_df, columns=['Correlation'])
    correlation_df.index.name = 'Habit'
    correlation_df['Correlation'] = correlation_df['Correlation'].apply(discretize_correlation)
    return habit_usage, productivity, correlation_df
