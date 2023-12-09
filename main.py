import csv
import mysql.connector

class SurfingData:
    def __init__(self, ID, WillingToBeInterviewed, LiveWithinLosAngelesCounty, Age, Race, Gender,
                 HasSurfingExperience, PrimaryBeach, PreferredSurfingTime, SurferLevel, SurfboardType,
                 SurfingFrequency, SurfingWithFriendsPercentage, FactorsInfluencingSurfing, FactorsInfluencingBeachChoice,
                 MetSomeoneInTheLineup, ComfortableMeetingNewPeople, RatingOfConversations, SocializingAfterSurfing,
                 AttendedCommunityEvents, ReceivedAdviceInWater, OfferedAdviceInWater, SocialMediaGroupsOrForums,
                 SharedSenseOfRespect, SupportiveCommunity, ComfortableAndAccepted, PerceivedGenderImbalance,
                 GenderInLineup, EncourageOthersToSurf, ConsideredStoppingSurfing, KnowSomeoneChangedSurfingHabits,
                 PreferToSurfAlone, SenseOfBelonging, ComfortEngagingWithStrangers):
        self.ID = ID
        self.WillingToBeInterviewed = WillingToBeInterviewed
        self.LiveWithinLosAngelesCounty = LiveWithinLosAngelesCounty
        self.Age = Age
        self.Race = Race
        self.Gender = Gender
        self.HasSurfingExperience = HasSurfingExperience
        self.PrimaryBeach = PrimaryBeach
        self.PreferredSurfingTime = PreferredSurfingTime
        self.SurferLevel = SurferLevel
        self.SurfboardType = SurfboardType
        self.SurfingFrequency = SurfingFrequency
        self.SurfingWithFriendsPercentage = SurfingWithFriendsPercentage
        self.FactorsInfluencingSurfing = FactorsInfluencingSurfing
        self.FactorsInfluencingBeachChoice = FactorsInfluencingBeachChoice
        self.MetSomeoneInTheLineup = MetSomeoneInTheLineup
        self.ComfortableMeetingNewPeople = ComfortableMeetingNewPeople
        self.RatingOfConversations = RatingOfConversations
        self.SocializingAfterSurfing = SocializingAfterSurfing
        self.AttendedCommunityEvents = AttendedCommunityEvents
        self.ReceivedAdviceInWater = ReceivedAdviceInWater
        self.OfferedAdviceInWater = OfferedAdviceInWater
        self.SocialMediaGroupsOrForums = SocialMediaGroupsOrForums
        self.SharedSenseOfRespect = SharedSenseOfRespect
        self.SupportiveCommunity = SupportiveCommunity
        self.ComfortableAndAccepted = ComfortableAndAccepted
        self.PerceivedGenderImbalance = PerceivedGenderImbalance
        self.GenderInLineup = GenderInLineup
        self.EncourageOthersToSurf = EncourageOthersToSurf
        self.ConsideredStoppingSurfing = ConsideredStoppingSurfing
        self.KnowSomeoneChangedSurfingHabits = KnowSomeoneChangedSurfingHabits
        self.PreferToSurfAlone = PreferToSurfAlone
        self.SenseOfBelonging = SenseOfBelonging
        self.ComfortEngagingWithStrangers = ComfortEngagingWithStrangers

# Initialize an empty list to store SurfingData objects
surfing_data_list = []

# Replace 'your_csv_file.csv' with the actual path to your CSV file
csv_file_path = 'data.csv'

# Open and read the CSV file
with open(csv_file_path, 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)

    # Skip the header row
    next(reader)

    # Loop through the rows in the CSV file

    for index, row in enumerate(reader):
        # Unpack the row values into variables
        timestamp, email, WillingToBeInterviewed, LiveWithinLosAngelesCounty, Age, Race, Gender, \
        HasSurfingExperience, PrimaryBeach, PreferredSurfingTime, SurferLevel, SurfboardType, \
        SurfingFrequency, SurfingWithFriendsPercentage, FactorsInfluencingSurfing, FactorsInfluencingBeachChoice, MetSomeoneInTheLineup, \
        ComfortableMeetingNewPeople, RatingOfConversations, SocializingAfterSurfing, AttendedCommunityEvents, \
        ReceivedAdviceInWater, OfferedAdviceInWater, SocialMediaGroupsOrForums, SharedSenseOfRespect, \
        SupportiveCommunity, ComfortableAndAccepted, PerceivedGenderImbalance, GenderInLineup, \
        EncourageOthersToSurf, ConsideredStoppingSurfing, KnowSomeoneChangedSurfingHabits, \
        PreferToSurfAlone, SenseOfBelonging, ComfortEngagingWithStrangers = row

        # Create a SurfingData object and append it to the list
        surfing_data = SurfingData(
            index, WillingToBeInterviewed, LiveWithinLosAngelesCounty, Age, Race, Gender,
            HasSurfingExperience, PrimaryBeach, PreferredSurfingTime, SurferLevel, SurfboardType,
            SurfingFrequency, SurfingWithFriendsPercentage, FactorsInfluencingSurfing, FactorsInfluencingBeachChoice,
            MetSomeoneInTheLineup, ComfortableMeetingNewPeople, RatingOfConversations, SocializingAfterSurfing,
            AttendedCommunityEvents, ReceivedAdviceInWater, OfferedAdviceInWater, SocialMediaGroupsOrForums,
            SharedSenseOfRespect, SupportiveCommunity, ComfortableAndAccepted, PerceivedGenderImbalance,
            GenderInLineup, EncourageOthersToSurf, ConsideredStoppingSurfing, KnowSomeoneChangedSurfingHabits,
            PreferToSurfAlone, SenseOfBelonging, ComfortEngagingWithStrangers
        )

        surfing_data_list.append(surfing_data)


# MySQL configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'password',
    'database': 'surf',
}

# Connect to the MySQL database
try:
    connection = mysql.connector.connect(**db_config)

    # Create a cursor object
    cursor = connection.cursor()

    # Insert SurfingData objects into the MySQL table
    for surfing_data in surfing_data_list:
        insert_query = """
        INSERT INTO SurfingData (WillingToBeInterviewed, LiveWithinLosAngelesCounty, Age, Race, Gender,
        HasSurfingExperience, PrimaryBeach, PreferredSurfingTime, SurferLevel, SurfboardType,
        SurfingFrequency, SurfingWithFriendsPercentage, FactorsInfluencingBeachChoice, MetSomeoneInTheLineup,
        ComfortableMeetingNewPeople, RatingOfConversations, SocializingAfterSurfing, AttendedCommunityEvents,
        ReceivedAdviceInWater, OfferedAdviceInWater, SocialMediaGroupsOrForums, SharedSenseOfRespect, SupportiveCommunity,
        ComfortableAndAccepted, PerceivedGenderImbalance, GenderInLineup, EncourageOthersToSurf, ConsideredStoppingSurfing,
        KnowSomeoneChangedSurfingHabits, PreferToSurfAlone, SenseOfBelonging, ComfortEngagingWithStrangers)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        data = (
            surfing_data.WillingToBeInterviewed, surfing_data.LiveWithinLosAngelesCounty, surfing_data.Age, surfing_data.Race,
            surfing_data.Gender, surfing_data.HasSurfingExperience, surfing_data.PrimaryBeach,
            surfing_data.PreferredSurfingTime, surfing_data.SurferLevel, surfing_data.SurfboardType,
            surfing_data.SurfingFrequency, surfing_data.SurfingWithFriendsPercentage, surfing_data.FactorsInfluencingBeachChoice,
            surfing_data.MetSomeoneInTheLineup, surfing_data.ComfortableMeetingNewPeople, surfing_data.RatingOfConversations, 
            surfing_data.SocializingAfterSurfing, surfing_data.AttendedCommunityEvents, surfing_data.ReceivedAdviceInWater, 
            surfing_data.OfferedAdviceInWater, surfing_data.SocialMediaGroupsOrForums, surfing_data.SharedSenseOfRespect, 
            surfing_data.SupportiveCommunity, surfing_data.ComfortableAndAccepted, surfing_data.PerceivedGenderImbalance, 
            surfing_data.GenderInLineup, surfing_data.EncourageOthersToSurf, surfing_data.ConsideredStoppingSurfing, 
            surfing_data.KnowSomeoneChangedSurfingHabits, surfing_data.PreferToSurfAlone, surfing_data.SenseOfBelonging, 
            surfing_data.ComfortEngagingWithStrangers
        )

        cursor.execute(insert_query, data)
        respondant_id = cursor.lastrowid  # Get the last inserted ID

        # Handle FactorsInfluencingSurfing field
        influencing_factors = surfing_data.FactorsInfluencingSurfing.split(',')
        for factor in influencing_factors:
            factor_insert_query = """
            INSERT INTO FactorsInfluencingSurfing (RespondantID, Reason)
            VALUES (%s, %s)
            """
            factor_data = (respondant_id, factor.strip())
            cursor.execute(factor_insert_query, factor_data)

    # Commit the changes and close the cursor and connection
    connection.commit()
    cursor.close()
    connection.close()

except mysql.connector.Error as error:
    print("MySQL Error: {}".format(error))
