#ifndef __DABIP_COMMON__COMMON_TYPES
#define __DABIP_COMMON__COMMON_TYPES

#include <vector>
#include <cstdint>

namespace dabip {
  using byte_vector_t = std::vector<std::uint8_t>;
  using pair_complete_vector_t = std::pair<bool, byte_vector_t>;
}



#endif // __DABIP_COMMON__COMMON_TYPES
