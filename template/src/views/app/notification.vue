<template>
  <div class="disable-text-selection">
    <b-row class="app-row survey-app">
      <b-colxx lg="2"></b-colxx>
      <b-colxx lg="10">
        <div class="mb-2 text-center">
          <h1>Notifications</h1>
        </div>
        <div class="separator mb-5" />
        <b-row key="itemList">
          <b-colxx
            xxs="12"
            v-for="(item, index) in Items"
            :key="`item${index}`"
          >
            <survey-list-item
              :key="item.id"
              :data="item"
              :selected-items="selectedItems"
              @toggle-item="toggleItem"
            />
          </b-colxx>
        </b-row>
      </b-colxx>
    </b-row>
  </div>
</template>

<script>
import { mapGetters, mapMutations, mapActions } from "vuex";
import SurveyListItem from "../../components/SurveyApp/SurveyListItem";

import axios from "axios";
import { apiUrl, api } from "../../constants/config";

export default {
  components: {
    "survey-list-item": SurveyListItem
  },
  data() {
    return {
      Items: [],
      sort: {
        column: "title",
        label: "Title"
      },
      sortOptions: [
        {
          column: "title",
          label: "Title"
        },
        {
          column: "category",
          label: "Category"
        },
        {
          column: "label",
          label: "Label"
        },
        {
          column: "status",
          label: "Status"
        }
      ],
      search: "",
      selectedItems: [],
      categories: [
        {
          label: "Development",
          value: "Development"
        },
        {
          label: "Workplace",
          value: "Workplace"
        },
        {
          label: "Hardware",
          value: "Hardware"
        }
      ],
      labels: [
        {
          label: "EDUCATION",
          value: "EDUCATION",
          color: "secondary"
        },
        {
          label: "NEW FRAMEWORK",
          value: "NEW FRAMEWORK",
          color: "primary"
        },
        {
          label: "PERSONAL",
          value: "PERSONAL",
          color: "info"
        }
      ],
      statuses: [
        {
          text: "ACTIVE",
          value: "ACTIVE"
        },
        {
          text: "COMPLETED",
          value: "COMPLETED"
        }
      ]
    };
  },
  computed: {
    ...mapGetters({
      currentUser: "currentUser"
    })
  },
  methods: {
    ...mapActions(["getSurveyItems"]),
    isSelectedAll() {
      return this.selectedItems.length >= this.surveyItems.length;
    },
    isAnyItemSelected() {
      return (
        this.selectedItems.length > 0 &&
        this.selectedItems.length < this.surveyItems.length
      );
    },
    loadItems() {
      const data = {
        id: this.currentUser.id
      };
      const data2 = {
        personId: this.currentUser.id
      };
      if (this.currentUser.role == "A") {
        axios
          .post(api + "SendRequestNotification/", data2)
          .then(response => {
            console.log(response);
            return response.data;
          })
          .then(res => {
            this.Items = res;
          });
      } else {
        axios
          .post(api + "showNotification/", data)
          .then(response => {
            console.log(response);
            return response.data;
          })
          .then(res => {
            this.Items = res;
          });
      }
    },

    changeOrderBy(sort) {
      this.sort = sort;
    },
    selectAll(isToggle) {
      if (this.selectedItems.length >= this.surveyItems.length) {
        if (isToggle) {
          this.selectedItems = [];
        }
      } else {
        this.selectedItems = this.surveyItems.map(x => x.id);
      }
    },
    keymap(event) {
      switch (event.srcKey) {
        case "select":
          this.selectAll(false);
          break;
        case "undo":
          this.selectedItems = [];
          break;
      }
    },
    getIndex(value, arr, prop) {
      for (var i = 0; i < arr.length; i++) {
        if (arr[i][prop] === value) {
          return i;
        }
      }
      return -1;
    },
    toggleItem(event, itemId) {
      if (event.shiftKey && this.selectedItems.length > 0) {
        let itemsForToggle = this.surveyItems;
        var start = this.getIndex(itemId, itemsForToggle, "id");
        var end = this.getIndex(
          this.selectedItems[this.selectedItems.length - 1],
          itemsForToggle,
          "id"
        );
        itemsForToggle = itemsForToggle.slice(
          Math.min(start, end),
          Math.max(start, end) + 1
        );
        this.selectedItems.push(
          ...itemsForToggle.map(item => {
            return item.id;
          })
        );
      } else {
        if (this.selectedItems.includes(itemId)) {
          this.selectedItems = this.selectedItems.filter(x => x !== itemId);
        } else {
          this.selectedItems.push(itemId);
        }
      }
    },
    handleContextmenu(vnode) {
      if (!this.selectedItems.includes(vnode.key)) {
        this.selectedItems = [vnode.key];
      }
    },
    onContextCopy() {
      console.log(
        "context menu item clicked - Copy Items: ",
        this.selectedItems
      );
    },
    onContextArchive() {
      console.log(
        "context menu item clicked - Move to Archive Items: ",
        this.selectedItems
      );
    },
    onContextDelete() {
      console.log(
        "context menu item clicked - Delete Items: ",
        this.selectedItems
      );
    }
  },
  mounted() {
    this.loadItems();
  }
};
</script>
