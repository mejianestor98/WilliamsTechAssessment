import gql from 'graphql-tag';

export const RACES_QUERY = gql`
query {
    races {
        id
        year
        name
    }
}`;

export const DRIVER_STANDINGS_QUERY = gql`
query GetDriverStandings($raceId: Int){
    driver_standings (race_id: $raceId){
        driver {
            id
            forename
            surname
            date_of_birth
            nationality
            code
            url
        }
        points
        position
    }
}`;

export const DRIVER_SUMMARY_QUERY = gql`
query GetDriverSummary($driverId: Int){
    driver_summary(driver_id: $driverId){
        career_podiums
        races_entered
    }
}
`;