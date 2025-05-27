<script setup>
import AnalyticsGlobalStats from '@/views/dashboard/AnalyticsGlobalStats.vue'
import AnalyticsProgrammingStats from '@/views/dashboard/AnalyticsProgrammingStats.vue'
import AnalyticsProgrammingTrends from '@/views/dashboard/AnalyticsProgrammingTrends.vue'
import AnalyticsRecentProgramming from '@/views/dashboard/AnalyticsRecentProgramming.vue'
</script>

<template>
  <VRow class="match-height">
    <!-- Global Programming Statistics -->
    <VCol cols="12">
      <AnalyticsGlobalStats />
    </VCol>

    <!-- Programming Language Cards -->
    <VCol
      cols="12"
      md="8"
    >
      <AnalyticsProgrammingStats />
    </VCol>

    <!-- Recent Programming Updates -->
    <VCol
      cols="12"
      md="4"
    >
      <AnalyticsRecentProgramming />
    </VCol>

    <!-- Programming Language Trends -->
    <VCol cols="12">
      <AnalyticsProgrammingTrends />
    </VCol>
  </VRow>
</template>
