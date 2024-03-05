from hypothesis import given, strategies as st
import numpy as np

effects_data = {'new_medication': [], 'existing_medication': []}


# Simulate the effect of medications on blood pressure
def new_medication_score(age, weight, baseline_bp):
    # New medication effectiveness depends on age, weight in kg and baseline blood pressure in bpm
    return baseline_bp - (10 + (age / 10) + (weight / 5) + np.random.normal(0, 5))


def existing_medication_score(baseline_bp):
    # Existing medication effectiveness is constant
    return baseline_bp - (15 + np.random.normal(0, 5))


# Strategy for generating patient profiles
patient_profile = st.fixed_dictionaries({
    'age': st.integers(18, 80),
    'weight': st.floats(50.0, 200.0),
    'baseline_bp': st.floats(120.0, 180.0)
})


# Patient profile
@given(patient_profile)
def test_medication_effectiveness(patient):
    age, weight, baseline_bp = patient['age'], patient['weight'], patient['baseline_bp']
    new_bp = new_medication_score(age, weight, baseline_bp)
    existing_bp = existing_medication_score(age, weight, baseline_bp)
    effects_data['new_medication'].append(baseline_bp - new_bp)
    effects_data['existing_medication'].append(baseline_bp - existing_bp)


test_medication_effectiveness()

# Calculate and print the average effect of each medication
average_new_medication_effect = np.mean(effects_data['new_medication'])
average_existing_medication_effect = np.mean(effects_data['existing_medication'])
print(f"Average effect of new medication: {average_new_medication_effect}")
print(f"Average effect of existing medication: {average_existing_medication_effect}")



# if __name__ == '__main':
#     test_medication_effectiveness(patient_profile)
#     print("Passed")
