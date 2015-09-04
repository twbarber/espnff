__author__ = 'Tyler'


def parse_rows(table):
    rows = table.findAll('tr')
    data = []
    for row in rows:
        cols = row.findAll('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])
    return data

class Table(object):

    def __init__(self, title, columns):
        self.title = title
        self.columns = columns
        self.rows = {}

    def add_row(self, row, values):
        self.rows[row] = values


class StandingsTable(object):

    def __init__(self):
        self.hide = False

    def __init__(self, hide):
        self.hide = hide

    def standings(self, table):
        data = parse_rows(table)
        standings = Table(data[0], data[1])
        for i, team in enumerate(data[2:8], start=1):
            entry = StandingsEntry(*team)
            standings.add_row(i, self.anonymize(i, entry))
        return standings

    def anonymize(self, i, entry):
        if self.hide:
            entry.name = 'Team ' + str(i)
        return entry


class StandingsDetailTable(object):
    def __init__(self):
        self.hide = False

    def __init__(self, hide):
        self.hide = hide

    def detail(self, table):
        data = parse_rows(table)
        standings_detail = Table(data[0], data[1])
        for i, team in enumerate(data[2:10], start=1):
            entry = DetailStandingsEntry(*team)
            standings_detail.add_row(i, self.anonymize(i, entry))
        return standings_detail

    def anonymize(self, i, entry):
        if self.hide:
            entry.name = 'Team ' + str(i)
        return entry


class RosterTable(object):
    def __init__(self):
        return

    def roster(self, table):
        data = parse_rows(table)
        starters = data[2:11]
        bench = data[13:20]
        full = starters + bench
        roster_table = Table('Roster', data[1])
        for i, team in enumerate(full, start=1):
            entry = RosterEntry(*team)
            roster_table.add_row(i, entry)
        return roster_table


class StandingsEntry(object):

    def __init__(self, name, win, loss, tie, pct, gb):
        self.name = name
        self.win = win
        self.loss = loss
        self.tie = tie
        self.pct = pct
        self.gb = gb

    def __repr__(self):
        string = (
            'Team:\t' + self.name + '\n' +
            'Wins:\t' + self.win + '\n' +
            'Loses:\t' + self.loss + '\n' +
            'Ties:\t' + self.tie + '\n' +
            'Pct:\t' + self.pct + '\n' +
            'GB:\t' + self.gb
        )
        return string

    def values(self):
        values = [
            self.name,
            self.win,
            self.loss,
            self.tie,
            self.pct,
            self.gb
        ]
        return values


class RosterEntry(object):

    def __init__(self, slot, player_team_pos, opp, status, prk, pts, avg, last, proj, oprk, start, own, add):
        self.slot = slot.encode('utf-8').strip()
        self.player_team_pos = player_team_pos.encode('utf-8').strip()
        self.opp = opp.encode('utf-8').strip()
        self.status = status.encode('utf-8').strip()
        self.prk = prk.encode('utf-8').strip()
        self.pts = pts.encode('utf-8').strip()
        self.avg = avg.encode('utf-8').strip()
        self.last = last.encode('utf-8').strip()
        self.proj = proj.encode('utf-8').strip()
        self.oprk = oprk.encode('utf-8').strip()
        self.start = start.encode('utf-8').strip()
        self.own = own.encode('utf-8').strip()
        self.add = add.encode('utf-8').strip()

    def __repr__(self):
        string = (
            'Slot:\t' + self.slot + '\n' +
            'Player:\t' + self.player_team_pos + '\n' +
            'Opponent:\t' + self.opp + '\n' +
            'Status:\t' + self.status + '\n' +
            'Prk:\t' + self.prk + '\n' +
            'Pts:\t' + self.pts + '\n' +
            'Avg:\t' + self.avg + '\n' +
            'Last:\t' + self.last + '\n' +
            'Proj:\t' + self.proj + '\n' +
            'Oprk:\t' + self.oprk + '\n' +
            'Start:\t' + self.start + '\n' +
            'Own:\t' + self.own + '\n' +
            'Add/Drop:\t' + self.add
        )
        return string

    def values(self):
        values = [
            self.slot,
            self.player_team_pos,
            self.opp,
            self.status,
            self.prk,
            self.pts,
            self.avg,
            self.last,
            self.proj,
            self.oprk,
            self.start,
            self.own,
            self.add
        ]
        return values



class DetailStandingsEntry(object):
    def __init__(self, club, pf, pa, home, away, div, streak):
        club_info = self.parse_club(club)
        if len(club_info) == 1:
            self.team = club_info[0]
            self.owner = ''
        else:
            self.team = club_info[0]
            self.owner = club_info[1]
        self.pf = pf
        self.pa = pa
        self.home = home
        self.away = away
        self.div = div
        self.streak = streak

    def __repr__(self):
        string = (
            'Team:\t' + self.team + '\n' +
            'Owner:\t' + self.owner + '\n' +
            'PF:\t' + self.pf + '\n' +
            'PA:\t' + self.pa + '\n' +
            'Home:\t' + self.home + '\n' +
            'Away:\t' + self.away + '\n' +
            'Div:\t' + self.div + '\n' +
            'Streak:\t' + self.streak + '\n'
        )
        return string

    def parse_club(self, club):
        club_info = club.split('(')
        if len(club_info) == 1:
            return club_info
        club_info[0] = club_info[0][:-1]
        club_info[1] = club_info[1][:-1]
        return club_info
