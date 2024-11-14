<script setup>
import gql from 'graphql-tag'
import { computed, ref, watch } from 'vue';
import { useQuery, useLazyQuery } from '@vue/apollo-composable';
import { RACES_QUERY, DRIVER_STANDINGS_QUERY, DRIVER_SUMMARY_QUERY } from '@/graphql/queries.js';

const { result, loading, error } = useQuery(RACES_QUERY);

const races = computed(() => result.value?.races ?? []);
const selectedRaceId = ref(null);

const fetchDriverStandings = ref(false);
const { result: driverStandingsResult, refetch: loadDriverStandings } = useQuery(DRIVER_STANDINGS_QUERY,
                                                                                 { raceId: selectedRaceId },
                                                                                 { enabled: fetchDriverStandings });
const driverStandings = computed(() => {
    return (driverStandingsResult.value?.driver_standings ?? [])
            .slice()
            .sort((a, b) => a.position - b.position);
});

watch(selectedRaceId, (newVal, oldVal) => {
    if (newVal) {
        clickedDriver.value = null;
        fetchDriverStandings.value = true;
        loadDriverStandings({ raceId: newVal });
    }
});

const clickedDriver = ref(null);
const fetchDriverSummary = ref(false);
const handleDriverClick = (driver) => {
    clickedDriver.value = driver;
    fetchDriverSummary.value = true;
    loadDriverSummary( {driverId : driver.id});
};

const { result: driverSummaryResult, refetch: loadDriverSummary } = useQuery(DRIVER_SUMMARY_QUERY,
                                                                             { driverId: clickedDriver.value ? clickedDriver.value.id : null },
                                                                             { enabled: fetchDriverSummary });

const driverSummary = computed(() => driverSummaryResult.value?.driver_summary ?? null);

</script>

<template>
    <div class="container-fluid">
        <div class="row mt-2">
            <div class="col-2">
                <select class="form-select" aria-label="Default select example" v-model="selectedRaceId">
                    <option selected>Select Race</option>
                    <option v-for="race in races" :key="race.id" :value="race.id">{{ race.year }} - {{ race.name }}
                    </option>
                </select>
            </div>
        </div>
        <div class="row mt-5">
            <div class="col-6">
                <table class="table table-dark table-striped table-hover">
                    <thead>
                        <tr>
                            <th scope="col">Pos</th>
                            <th scope="col">Driver</th>
                            <th scope="col">Points</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="driverStanding in driverStandings"
                            :key="driverStanding.driver.id"
                            @click="handleDriverClick(driverStanding.driver)">
                            <th scope="row">{{ driverStanding.position }}</th>
                            <td>{{ driverStanding.driver.forename }} {{ driverStanding.driver.surname }}</td>
                            <td>{{ driverStanding.points }}</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <div class="col-6" v-if="clickedDriver">
                <h1>{{ clickedDriver.forename }} {{ clickedDriver.surname }}</h1>
                <h2>{{ clickedDriver.code }}</h2>
                <h5> {{ clickedDriver.date_of_birth }} - {{ clickedDriver.nationality }}</h5>
                <p>Races entered: {{ driverSummary?.races_entered }}</p>
                <p>Career podiums: {{ driverSummary?.career_podiums }}</p>
                <a :href="clickedDriver.url" target="_blank">Wikipedia page</a>
            </div>
        </div>
    </div>
</template>

<style scoped>
tr {
    cursor: pointer;
}
</style>