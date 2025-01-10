import pandas as pd
from faker import Faker
import sys
from faker.providers import DynamicProvider


def get_dataset(record_count):
    state_data = pd.read_csv("./indian_states.csv")
    state_name_list = state_data['Name'].to_list()
    indian_state_provider = DynamicProvider(provider_name='indian_state', elements=state_name_list)

    fake = Faker()
    fake.add_provider(indian_state_provider)
    output_list = []
    for i in range(record_count):
        my_custom_record = dict()
        my_custom_record['LAN'] = fake.uuid4()
        my_custom_record['state'] = fake.indian_state()
        my_custom_record['amount'] = fake.pyfloat(min_value=50000.00, max_value=500000.00, right_digits=2)
        output_list.append(my_custom_record)
    #print(f'This is the generated output ===> {output_list}')
    output_df = pd.DataFrame(output_list)
    #output_df.to_csv("./output.csv", index=False)
    return output_df

def main():
    count = sys.argv[1]
    output_file_name = sys.argv[2]
    df = get_dataset(int(count))
    df.to_csv(f'./{output_file_name}', index=False)
    print('output csv created.')

if __name__ == '__main__':
    main()
