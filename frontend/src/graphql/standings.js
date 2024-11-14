import gql from "graphql-tag";

export const RACES_QUERY = gql`
query {
    races {
        id
        year
        name
    }
}
`;