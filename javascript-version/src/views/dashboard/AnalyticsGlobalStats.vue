<script setup>
import { ref, onMounted, computed } from 'vue'
import programmingData from '@/data/programming-stats.json'

const globalStats = ref({})

onMounted(() => {
  globalStats.value = programmingData.globalStats
})

const statistics = computed(() => [
  {
    title: 'Total Developers',
    stats: formatNumber(globalStats.value.totalActiveDevelopers),
    icon: 'ri-group-line',
    color: 'primary',
  },
  {
    title: 'Total Repositories',
    stats: formatNumber(globalStats.value.totalRepositories),
    icon: 'ri-git-repository-line',
    color: 'success',
  },
  {
    title: 'Monthly Growth',
    stats: globalStats.value.averageMonthlyGrowth + '%',
    icon: 'ri-line-chart-line',
    color: 'warning',
  },
  {
    title: 'Most Popular Field',
    stats: globalStats.value.mostPopularField,
    icon: 'ri-code-box-line',
    color: 'info',
  },
])

const formatNumber = (num) => {
  if (num >= 1000000) {
    return (num / 1000000).toFixed(1) + 'M'
  }
  if (num >= 1000) {
    return (num / 1000).toFixed(1) + 'K'
  }
  return num
}
</script>

<template>
  <VCard title="Global Programming Statistics">
    <template #subtitle>
      <p class="text-body-1 mb-0">
        Fastest Growing: <span class="font-weight-medium text-primary">{{ globalStats.fastestGrowingLanguage }}</span>
      </p>
    </template>

    <VCardText class="pt-6">
      <VRow>
        <VCol
          v-for="item in statistics"
          :key="item.title"
          cols="12"
          sm="6"
          md="3"
        >
          <div class="d-flex align-center gap-x-3">
            <VAvatar
              :color="item.color"
              rounded
              size="42"
              class="elevation-1"
            >
              <VIcon
                size="24"
                :icon="item.icon"
              />
            </VAvatar>

            <div class="d-flex flex-column">
              <div class="text-caption">
                {{ item.title }}
              </div>
              <h6 class="text-h6">
                {{ item.stats }}
              </h6>
            </div>
          </div>
        </VCol>
      </VRow>
    </VCardText>
  </VCard>
</template> 