<template>
  <div class="icon-cards-row" >
    <glide-component :settings="glideIconsOption">
      <icon-card @update="VideoQuality" :title="$t('Video Quality')" icon="iconsminds-like" :value="data.videoqualityCount" />
      <icon-card @update="ContentQuality" :title="$t('Content Quality')" icon="iconsminds-like" :value="data.contenqualitycount" />
      <icon-card
        @update="CourseDepth" 
        :title="$t('Course Covergae')"
        icon="iconsminds-like"
        :value="data.coursedepthCount"
      />
      <icon-card
        @update="CoursePace" 
        :title="$t('Course Pace')"
        icon="iconsminds-like"
        :value="data.courpacethCount"
      />
      <icon-card
        @update="QualifiedInstructor" 
        :title="$t('Qualified Instructor')"
        icon="iconsminds-like"
        :value="data.qualifiedinstructorCount"
      />
    </glide-component>
  </div>
</template>

<script>
import GlideComponent from "../../components/Carousel/GlideComponent";
import IconCard from "../../components/Cards/IconCard";

export default {
  props: ['data','VideoQuality','ContentQuality','CourseDepth','CoursePace','QualifiedInstructor'],
  components: {
    "glide-component": GlideComponent,
    "icon-card": IconCard
  },
  data() {
    return {
      glideIconsOption: {
        gap: 5,
        perView: 5,
        type: "carousel",
        hideNav: true
      }
    };
  }
};
</script>
