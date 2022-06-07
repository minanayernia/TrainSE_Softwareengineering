<template>
  <router-link to="/app/resourceDetail" class="w-40 w-sm-100">
    <b-card
      :class="{
        'd-flex flex-row': true,
        active: selectedItems.includes(data.id)
      }"
      no-body
    >
      <div class="pl-2 d-flex flex-grow-1 min-width-zero">
        <div
          class="card-body align-self-center d-flex flex-column flex-lg-row justify-content-between min-width-zero align-items-lg-center"
        >
          <p class="list-item-heading mb-0 truncate">{{ data.title }}</p>
          <p class="mb-0 text-muted text-small w-15 w-sm-100">
            {{ data.category }}
          </p>
          <p class="mb-0 text-muted text-small w-15 w-sm-100">
            {{ data.date }}
          </p>
          <div class="w-15 w-sm-100">
            <b-badge pill :variant="data.statusColor">{{
              data.status
            }}</b-badge>
          </div>
        </div>
      </div>
    </b-card>
  </router-link>
</template>

<script>
export default {
  props: ["data", "selectedItems"],
  methods: {
    toggleItem(event, itemId) {
      this.$emit("toggle-item", event, itemId);
    }
  }
};
</script>
