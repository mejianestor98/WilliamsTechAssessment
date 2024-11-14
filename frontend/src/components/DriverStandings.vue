<script setup>
import { computed, ref, watch } from 'vue';
import { useQuery } from '@vue/apollo-composable';
import { RACES_QUERY } from '@/graphql/standings.js';

const { result, loading, error } = useQuery(RACES_QUERY);

const races = computed(() => result.value?.races ?? []);
const selectedRaceId = ref(null);

watch(selectedRaceId, (newVal, oldVal) => {
    console.log(`Selected race ID changed from ${oldVal} to ${newVal}`);
});

</script>


<template>
    <div class="container-fluid">
        <div class="row mt-2">
            <div class="col-2">
                <select class="form-select" aria-label="Default select example" v-model="selectedRaceId">
                    <option selected>Select Race</option>
                    <option v-for="race in races" :key="race.id" :value="race.id">{{ race.year }} - {{ race.name }}</option>
                </select>
            </div>
        </div>
    </div>
</template>

<style scoped></style>