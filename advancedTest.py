from hypothesis import given, strategies as st
import numpy as np

effects_data = {
    'new_medication': [],
    'existing_medication': []
}


# Simulate the effect of medications on blood pressure
def new_medication_score(age, weight, baseline_bp):
    # New medication effectiveness depends on age, weight in kg and baseline blood pressure in bpm
    return baseline_bp - (10 + (age / 10) + (weight / 5))


def existing_medication_score(age, weight, baseline_bp):
    # Existing medication effectiveness only depends on weight
    return baseline_bp - (weight / 10) - 25


# Strategy for generating patient profiles
patient_profile = st.fixed_dictionaries({
    'age': st.integers(18, 100),
    'weight': st.floats(30, 300),
    'baseline_bp': st.floats(30, 190)
})


# Patient profile
@given(patient_profile)
def test_medication_effectiveness(patient):
    age, weight, baseline_bp = patient['age'], patient['weight'], patient['baseline_bp']
    new_bp = new_medication_score(age, weight, baseline_bp)
    existing_bp = existing_medication_score(age, weight, baseline_bp)
    effects_data['new_medication'].append(new_bp)
    effects_data['existing_medication'].append(existing_bp)


test_medication_effectiveness()

# Calculate and print the average effect of each medication
# Also print the result of which medication is better
average_new_medication_effect = np.mean(effects_data['new_medication'])
average_existing_medication_effect = np.mean(effects_data['existing_medication'])
print(f"Average effect of new medication: {average_new_medication_effect}.")
print(f"Average effect of existing medication: {average_existing_medication_effect}.\n")
if average_new_medication_effect > average_existing_medication_effect:
    print("Your new medication is better.")
else:
    print("Your old medication was better.")
