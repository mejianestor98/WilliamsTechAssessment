<script setup>
import gql from 'graphql-tag'
import { computed, ref, watch } from 'vue';
import { useQuery, useLazyQuery } from '@vue/apollo-composable';
import { RACES_QUERY, DRIVER_STANDINGS_QUERY } from '@/graphql/standings.js';

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
    console.log(`Selected race ID changed from ${oldVal} to ${newVal}`);
    if (newVal) {
        clickedDriver.value = null;
        fetchDriverStandings.value = true;
        loadDriverStandings({ raceId: newVal });
    }
});

const clickedDriver = ref(null)
const handleDriverClick = (driver) => {
    console.log(driver)
    clickedDriver.value = driver
};

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
                <h1>{{ clickedDriver.surname }}</h1>
                <h3>{{ clickedDriver.forename }}</h3>
                <h2>{{ clickedDriver.code }}</h2>
                <p> {{ clickedDriver.date_of_birth }} - {{ clickedDriver.nationality }}</p>
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