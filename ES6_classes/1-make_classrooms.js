import ClassRoom from "./0-classroom";

export default function initializeRooms() {
  const roomSizes = [19, 20, 34];
  const newRooms = roomSizes.map(roomSize => new ClassRoom(roomSize));

  return newRooms;
}
