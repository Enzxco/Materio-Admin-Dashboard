<script setup>
import avatar1 from '@/assets/images/avatars/kevin-law.jpg'
import avatar2 from '@images/avatars/avatar-2.png'
import avatar3 from '@images/avatars/avatar-3.png'
import avatar4 from '@images/avatars/avatar-4.png'
import avatar5 from '@images/avatars/avatar-5.png'

const activities = [
  {
    id: 1,
    avatar: avatar1,
    user: 'Sarah Chen',
    action: 'committed to',
    target: 'TypeScript Core',
    details: 'Improved type inference in generic functions',
    time: '25 mins ago',
    commit: 'abc123f',
    type: 'commit',
    language: 'TypeScript'
  },
  {
    id: 2,
    avatar: avatar2,
    user: 'John Miller',
    action: 'opened issue in',
    target: 'Python Django',
    details: 'Bug: Async view performance regression',
    time: '2 hours ago',
    issueNumber: '#1234',
    type: 'issue',
    language: 'Python'
  },
  {
    id: 3,
    avatar: avatar3,
    user: 'Emma Wilson',
    action: 'merged PR in',
    target: 'React Core',
    details: 'Add new concurrent rendering features',
    time: '5 hours ago',
    prNumber: '#567',
    type: 'pull-request',
    language: 'JavaScript'
  },
  {
    id: 4,
    avatar: avatar4,
    user: 'Alex Kumar',
    action: 'released version',
    target: 'Spring Framework',
    details: 'Version 6.1.0 with security patches',
    time: '1 day ago',
    version: 'v6.1.0',
    type: 'release',
    language: 'Java'
  },
  {
    id: 5,
    avatar: avatar5,
    user: 'Maria Garcia',
    action: 'created branch in',
    target: 'C++ Standard',
    details: 'Feature implementation for C++23',
    time: '2 days ago',
    branch: 'feature/cpp23',
    type: 'branch',
    language: 'C++'
  }
]

const getActionIcon = (type) => {
  switch (type) {
    case 'commit':
      return 'ri-git-commit-line'
    case 'issue':
      return 'ri-error-warning-line'
    case 'pull-request':
      return 'ri-git-pull-request-line'
    case 'release':
      return 'ri-rocket-line'
    case 'branch':
      return 'ri-git-branch-line'
    default:
      return 'ri-code-line'
  }
}

const getActionColor = (type) => {
  switch (type) {
    case 'commit':
      return 'primary'
    case 'issue':
      return 'warning'
    case 'pull-request':
      return 'success'
    case 'release':
      return 'info'
    case 'branch':
      return 'error'
    default:
      return 'secondary'
  }
}

const handleActivityClick = (activity) => {
  // This would typically open the relevant link/action
  switch (activity.type) {
    case 'commit':
      console.log('View commit: ' + activity.commit)
      break
    case 'issue':
      console.log('View issue: ' + activity.issueNumber)
      break
    case 'pull-request':
      console.log('View PR: ' + activity.prNumber)
      break
    case 'release':
      console.log('View release: ' + activity.version)
      break
    case 'branch':
      console.log('View branch: ' + activity.branch)
      break
  }
}
</script>

<template>
  <VCard>
    <VCardItem>
      <VCardTitle>Recent Activities</VCardTitle>
      <template #append>
        <VBtn
          variant="text"
          color="default"
          size="small"
          class="me-n3"
        >
          View All
        </VBtn>
      </template>
    </VCardItem>

    <VCardText>
      <VList class="card-list">
        <VListItem
          v-for="activity in activities"
          :key="activity.id"
          @click="handleActivityClick(activity)"
          class="activity-item"
        >
          <template #prepend>
            <VAvatar
              size="38"
              :image="activity.avatar"
            />
          </template>

          <VListItemTitle class="font-weight-medium mb-1">
            <span class="text-high-emphasis">{{ activity.user }}</span>
            <span class="text-medium-emphasis"> {{ activity.action }} </span>
            <span class="text-primary">{{ activity.target }}</span>
          </VListItemTitle>

          <VListItemSubtitle class="d-flex align-center gap-2">
            <VIcon
              :icon="getActionIcon(activity.type)"
              :color="getActionColor(activity.type)"
              size="16"
            />
            <span class="text-body-2">{{ activity.details }}</span>
          </VListItemSubtitle>

          <template #append>
            <div class="d-flex flex-column align-end">
              <VChip
                :color="getActionColor(activity.type)"
                size="x-small"
                class="mb-1"
                label
              >
                {{ activity.language }}
              </VChip>
              <span class="text-xs text-medium-emphasis">{{ activity.time }}</span>
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

.activity-item {
  cursor: pointer;
  transition: background-color 0.2s ease;

  &:hover {
    background-color: rgb(var(--v-theme-surface-variant));
  }
}

.text-xs {
  font-size: 0.75rem;
}
</style>
