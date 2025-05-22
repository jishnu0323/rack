package com.RackSystemApplication.Repository;

import com.RackSystemApplication.Entity.RackItem;
import org.springframework.data.jpa.repository.JpaRepository;

public interface RackItemRepository extends JpaRepository<RackItem, Long> {
}