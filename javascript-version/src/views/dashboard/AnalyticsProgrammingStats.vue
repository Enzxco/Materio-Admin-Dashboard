<script setup>
import { ref, onMounted } from 'vue'
import programmingData from '@/data/programming-stats.json'

const languages = ref([])
const globalStats = ref({})

onMounted(() => {
  languages.value = programmingData.languages
  globalStats.value = programmingData.globalStats
})

const getLanguageColor = (index) => {
  const colors = ['primary', 'success', 'warning', 'error', 'info']
  return colors[index % colors.length]
}

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
  <VCard>
    <VCardItem>
      <VCardTitle>Programming Languages Overview</VCardTitle>
      <template #append>
        <div class="text-caption">
          Last Updated: {{ globalStats.lastUpdated }}
        </div>
      </template>
    </VCardItem>

    <VCardText>
      <VRow>
        <VCol
          v-for="(lang, index) in languages"
          :key="lang.id"
          cols="12"
          sm="6"
          md="4"
          lg="4"
        >
          <VCard
            :color="getLanguageColor(index)"
            variant="tonal"
          >
            <VCardItem>
              <VCardTitle>{{ lang.name }}</VCardTitle>
              <template #append>
                <VIcon
                  size="24"
                  :icon="lang.trend.yearOverYearGrowth > 10 ? 'ri-rocket-2-line' : 'ri-code-line'"
                />
              </template>
            </VCardItem>

            <VCardText>
              <div class="d-flex justify-space-between align-center mb-2">
                <span class="text-subtitle-2">Popularity</span>
                <span class="text-h6">{{ lang.stats.popularity }}%</span>
              </div>
              <VProgressLinear
                :model-value="lang.stats.popularity"
                :color="getLanguageColor(index)"
                height="8"
                rounded
              />

              <div class="mt-4 d-flex justify-space-between">
                <div>
                  <div class="text-caption">Active Users</div>
                  <div class="text-body-1 font-weight-medium">
                    {{ formatNumber(lang.stats.activeUsers) }}
                  </div>
                </div>
                <div>
                  <div class="text-caption">GitHub Repos</div>
                  <div class="text-body-1 font-weight-medium">
                    {{ formatNumber(lang.stats.githubRepos) }}
                  </div>
                </div>
                <div>
                  <div class="text-caption">Monthly Growth</div>
                  <div class="text-body-1 font-weight-medium">
                    {{ lang.stats.monthlyGrowth }}%
                  </div>
                </div>
              </div>
            </VCardText>
          </VCard>
        </VCol>
      </VRow>
    </VCardText>
  </VCard>
</template>

<style lang="scss" scoped>
.v-card {
  transition: transform 0.2s;

  &:hover {
    transform: translateY(-4px);
  }
}
</style> 