<script setup>
import { ref, onMounted } from 'vue'
import programmingData from '@/data/programming-stats.json'

const languages = ref([])
const recentUpdates = [
  {
    language: 'TypeScript',
    event: 'Major Version Release',
    details: 'TypeScript 5.4 released with improved type inference',
    date: '2024-03-15',
    icon: 'ri-code-box-line',
    color: 'primary'
  },
  {
    language: 'Python',
    event: 'Framework Update',
    details: 'Django 5.0 introduces async views improvements',
    date: '2024-03-14',
    icon: 'ri-database-2-line',
    color: 'success'
  },
  {
    language: 'JavaScript',
    event: 'Package Release',
    details: 'React 19 beta introduces new concurrent features',
    date: '2024-03-13',
    icon: 'ri-reactjs-line',
    color: 'info'
  },
  {
    language: 'Java',
    event: 'Security Update',
    details: 'Spring Boot 3.2.1 patches security vulnerabilities',
    date: '2024-03-12',
    icon: 'ri-shield-check-line',
    color: 'warning'
  },
  {
    language: 'C++',
    event: 'Standard Update',
    details: 'C++23 features finalized for upcoming release',
    date: '2024-03-11',
    icon: 'ri-terminal-box-line',
    color: 'error'
  }
]

onMounted(() => {
  languages.value = programmingData.languages
})

const getStatusColor = (language) => {
  const lang = languages.value.find(l => l.name === language)
  return lang && lang.stats.monthlyGrowth > 1.5 ? 'success' : 'secondary'
}
</script>

<template>
  <VCard title="Recent Programming Updates">
    <template #subtitle>
      <span class="text-body-1">Latest updates and releases in programming languages</span>
    </template>

    <VCardText>
      <VList class="card-list">
        <VListItem
          v-for="update in recentUpdates"
          :key="update.language"
        >
          <template #prepend>
            <VAvatar
              :color="update.color"
              variant="tonal"
              rounded
            >
              <VIcon
                :icon="update.icon"
                size="24"
              />
            </VAvatar>
          </template>

          <VListItemTitle class="font-weight-semibold mb-1">
            {{ update.event }}
            <VChip
              :color="getStatusColor(update.language)"
              size="x-small"
              class="ms-2"
              label
            >
              {{ update.language }}
            </VChip>
          </VListItemTitle>

          <VListItemSubtitle class="text-body-1">
            {{ update.details }}
          </VListItemSubtitle>

          <template #append>
            <div class="text-caption text-medium-emphasis">
              {{ update.date }}
            </div>
          </template>
        </VListItem>
      </VList>
    </VCardText>
  </VCard>
</template>

<style lang="scss" scoped>
.card-list {
  --v-card-list-gap: 1rem;
}

.v-list-item {
  padding-block: 0.7rem;
}
</style> 