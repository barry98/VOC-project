import pandas as pd
from datetime import datetime

def annotate(df, prev=None):
    if prev is not None:
        final = prev.copy()
        start = len(final)
    else:
        final = pd.DataFrame(columns = df.columns)
        final['vocop_match'] = None
        start = 0
    holder = []
    #stop = False
    #while stop != True:
    c = 0
    for row in df[start:].itertuples():
        answer = None
        c += 1
        if c == 21:
            print('Saving current progress.')
            final['vocop_match'][start:] = holder
            final.to_json('result.json')
            c = 0
        notary_date = datetime.strptime(row.datering, '%Y-%m-%d')
        if row.data_matches != 0 and row.data_matches != '0':
            #print(row.data_matches)
            #for person in row.data_matches:
            for person in row.data_matches:
                try:
                    out_date = datetime.strptime(person['date_out'], '%Y-%m-%d')
                except:
                    out_date = datetime(year=1, month=1, day =1 )
                try:
                    return_date = datetime.strptime(person['date_return'], '%Y-%m-%d')
                except:
                    return_date = datetime(year=1, month=1, day =1 )
                if (notary_date - out_date).days not in range(0, -91, -1) and (notary_date - return_date).days not in range(0, 91):
                    #print('Skipped match')
                    continue

                else:
                    print('{:10} | {:30} | {}'.format(' ', "Notary Information " + str(row.Index), 'VOC Information ' + str(person['index'])))
                    print('-' * 108)
                    print('{:10} | {:30} | {} / {}'.format('Name', row.name, person['name_original'], person['name_normalized']))
                    print('{:10} | {:30} | {} / {}'.format('Dates', row.datering, person['date_out'], person['date_return']))
                    print('{:10} | {:30} | {} / {}'.format('Ships', ' / '.join(row.data_entry[str(person['index'])]['ships']), person['ship_out'], person['ship_return']))
                    print('{:10} | {:30} | {}'.format('Rank', ' / '.join(row.data_entry[str(person['index'])]['rank']), person['rank']))
                    print('{:10} | {:30} | {}'.format('Locations', ' / '.join(row.data_entry[str(person['index'])]['location']), person['place_of_origin']))
                    check = False
                    print('Are these persons the same? y/n:')
                    while check != True:
                        answer = input()
                        if answer == 'y':
                            holder.append((person['name_original'], person['index']))
                            final = final.append(df.loc[row.Index])
                            check = True
                        elif answer == 'n':
                            check = True
                        elif answer == 'text':
                            print(row.text)
                        elif answer == 'stop':
                            final['vocop_match'][start:] = holder
                            return final
                        else:
                            print("Invalid input please enter 'y', 'n', 'stop', or 'text' without the quotes.")
                    if answer == 'y':
                        break
                    else:
                        continue
            if answer == 'y':
                continue
            else:
                holder.append(0)
                final = final.append(df.loc[row.Index])
        else:
            holder.append(0)
            final = final.append(df.loc[row.Index])
    final['vocop_match'][start:] = holder
    return final



subset = pd.read_json('annotationsubset.json')
try:
    prev = pd.read_json('result.json')
    df = annotate(subset, prev)
except ValueError:
    df = annotate(subset)

df.to_json('result.json')