CREATE TABLE SurfingData (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    WillingToBeInterviewed ENUM('Yes', 'No'),
    LiveWithinLosAngelesCounty ENUM('Yes', 'No'),
    Age INT,
    Race VARCHAR(50),
    Gender VARCHAR(50),
    HasSurfingExperience ENUM('Yes', 'No'),
    PrimaryBeach VARCHAR(100),
    PreferredSurfingTime VARCHAR(100),
    SurferLevel VARCHAR(50),
    SurfboardType VARCHAR(100),
    SurfingFrequency INT,
    SurfingWithFriendsPercentage INT,
    FactorsInfluencingBeachChoice VARCHAR(255),
    MetSomeoneInTheLineup ENUM('Yes', 'No'),
    ComfortableMeetingNewPeople ENUM('Yes', 'No'),
    RatingOfConversations INT,
    SocializingAfterSurfing INT,
    AttendedCommunityEvents ENUM('Yes', 'No'),
    ReceivedAdviceInWater ENUM('Yes', 'No'),
    OfferedAdviceInWater ENUM('Yes', 'No'),
    SocialMediaGroupsOrForums ENUM('Yes', 'No'),
    SharedSenseOfRespect INT,
    SupportiveCommunity INT,
  	ComfortableAndAccepted INT,
    PerceivedGenderImbalance INT,
    GenderInLineup INT,
    EncourageOthersToSurf INT,
    ConsideredStoppingSurfing INT,
    KnowSomeoneChangedSurfingHabits ENUM('Yes', 'No'),
    PreferToSurfAlone INT,
    SenseOfBelonging INT,
    ComfortEngagingWithStrangers INT 
);

CREATE TABLE FactorsInfluencingSurfing (
  ID INT AUTO_INCREMENT PRIMARY KEY,
  RespondantID INT,
  Reason VARCHAR(100),
);
