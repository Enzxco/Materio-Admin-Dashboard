<script setup>
import { ref, watch, nextTick } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const props = defineProps({
  isOpen: {
    type: Boolean,
    required: true,
  },
})

const emit = defineEmits(['update:isOpen', 'search'])

const searchQuery = ref('')
const searchResults = ref([])

// Mock data for demonstration - replace with actual data
const mockItems = [
  { title: 'Dashboard', path: '/dashboard' },
  { title: 'Account Settings', path: '/pages/account-settings' },
  { title: 'User Management', path: '/apps/users' },
  { title: 'Programming Stats', path: '/programming-stats' },
]

const performSearch = () => {
  if (!searchQuery.value) {
    searchResults.value = []
    return
  }

  // Filter items based on search query
  searchResults.value = mockItems.filter(item =>
    item.title.toLowerCase().includes(searchQuery.value.toLowerCase())
  )

  emit('search', searchQuery.value)
}

const closeDialog = () => {
  searchQuery.value = ''
  searchResults.value = []
  emit('update:isOpen', false)
}

const navigateToResult = (path) => {
  closeDialog()
  router.push(path)
}

// Watch for dialog opening to focus input
const searchInput = ref(null)
watch(() => props.isOpen, (newVal) => {
  if (newVal) {
    // Use nextTick to ensure the dialog is mounted
    nextTick(() => {
      searchInput.value?.focus()
    })
  }
})
</script>

<template>
  <VDialog
    v-model="props.isOpen"
    class="search-dialog"
    max-width="550"
    @keydown.esc="closeDialog"
  >
    <VCard>
      <VCardText>
        <!-- Search Input -->
        <div class="d-flex align-center py-2">
          <VIcon
            icon="ri-search-line"
            class="me-3"
          />
          <VTextField
            ref="searchInput"
            v-model="searchQuery"
            placeholder="Search (Press '/' to focus)"
            variant="plain"
            density="compact"
            hide-details
            @input="performSearch"
            @keydown.esc="closeDialog"
            @keydown.enter="searchResults.length && navigateToResult(searchResults[0].path)"
          />
          <VIcon
            icon="ri-close-line"
            class="ms-3 cursor-pointer"
            @click="closeDialog"
          />
        </div>

        <!-- Search Results -->
        <VDivider class="my-2" />

        <VList v-if="searchResults.length" class="search-results">
          <VListItem
            v-for="result in searchResults"
            :key="result.path"
            :value="result"
            @click="navigateToResult(result.path)"
          >
            <template #prepend>
              <VIcon
                icon="ri-arrow-right-line"
                size="small"
              />
            </template>

            <VListItemTitle>{{ result.title }}</VListItemTitle>
            <VListItemSubtitle class="text-disabled">
              {{ result.path }}
            </VListItemSubtitle>
          </VListItem>
        </VList>

        <div
          v-else-if="searchQuery"
          class="pa-4 text-center text-disabled"
        >
          No results found for "{{ searchQuery }}"
        </div>

        <div
          v-else
          class="pa-4 text-center text-disabled"
        >
          Type to search or press ESC to close
        </div>

        <!-- Keyboard Shortcuts -->
        <div class="d-flex justify-space-between align-center pa-2 text-disabled text-caption">
          <div>
            <span class="me-2">↵ to select</span>
            <span class="me-2">↑↓ to navigate</span>
          </div>
          <div>ESC to close</div>
        </div>
      </VCardText>
    </VCard>
  </VDialog>
</template>

<style lang="scss" scoped>
.search-dialog {
  .v-card {
    border-radius: 8px;
  }

  .v-text-field {
    font-size: 1.1rem;

    input {
      border: none !important;
      background: transparent !important;
    }
  }

  .search-results {
    max-height: 400px;
    overflow-y: auto;
  }

  .v-list-item {
    min-height: 48px;
    padding: 8px 16px;
    cursor: pointer;

    &:hover {
      background: rgba(var(--v-theme-primary), 0.05);
    }
  }
}
</style>
