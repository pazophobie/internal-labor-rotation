import pandas as pd
import numpy as np

def gsc_algorithm(workers,managers,df1,df2,df3):
    
    def rank_from___of___(a, b):
        if a in workers:
            if not df1.loc[df1[a] == b].empty:
                return float(df1.loc[df1[a] == b]['Rank'])
            else:
                return np.nan

        elif a in managers:
            if not df2.loc[df2[a] == b].empty:
                return float(df2.loc[df2[a] == b]['Rank'])
            else:
                return np.nan

    """Create final matching dataframe """
    gsc_outcome = pd.DataFrame(index=workers, columns=[0, 1])
    for s in workers:
        gsc_outcome.loc[s][0] = s

    """ The gsc Algorithm """

    """ create lists in which unmatched workers and managers will be put into during the algorithm"""
    matched_workers_gsc = []
    matched_managers_gsc = []


    """ The story """

    story = pd.DataFrame(index=[(0)], columns=[(0)])
    story_line = pd.DataFrame(index=[(0)], columns=[(0)])


    """Algorithm"""

    for i in range(0, 63):
        workers = [x for x in workers if x not in matched_workers_gsc]
        managers = [x for x in managers if x not in matched_managers_gsc]

        for p in workers:
            for m in managers:
                if (rank_from___of___(p,m), rank_from___of___(m,p)) == (float(df3.loc[i]['Participant']), float(df3.loc[i]['Manager'])):

                    story_line[0] = ''.join(['In step ',str(i+1),': ', p,' is matched to ', m,'. This is a ', str(df3.loc[i]['Participant']), ':',str(df3.loc[i]['Manager']) ])
                    story = story.append(story_line)

                    gsc_outcome.loc[p][1] = m
                    matched_workers_gsc.extend([p])
                    matched_managers_gsc.extend([m])


    story = story.reset_index()
    story = story.drop(['index'], 1)
    story = story.drop(0)

    return gsc_outcome, story


